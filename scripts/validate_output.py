"""Valida a estrutura e os contratos declarativos do GEO OS."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


SKILL_NAMES = (
    "geo-diagnosis",
    "entity-map",
    "ai-search-testing",
    "answer-blocks",
    "citation-engineering",
)

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "skills/geo-diagnosis/SKILL.md",
    "skills/entity-map/SKILL.md",
    "skills/ai-search-testing/SKILL.md",
    "skills/answer-blocks/SKILL.md",
    "skills/citation-engineering/SKILL.md",
    "modules/intent-map.md",
    "modules/evidence-ledger.md",
    "modules/answer-blocks.md",
    "modules/citation-engineering.md",
    "rubrics/geo-readiness.yaml",
    "rubrics/citation-readiness.yaml",
    "rubrics/entity-authority.yaml",
    "templates/audit-report.md",
    "templates/entity-map.csv",
    "templates/ai-search-benchmark.csv",
    "templates/evidence-ledger.csv",
    "templates/answer-block-template.md",
    "templates/citation-opportunity-map.csv",
    "datasets/golden/benchmark-prompts-pt-br.json",
    "scripts/validate_output.py",
    "tests/test_validate_output.py",
    "docs/methodology.md",
    "docs/update-policy.md",
    "docs/source-ledger.md",
)

REQUIRED_SKILL_SECTIONS = (
    "objetivo",
    "quando usar",
    "quando não usar",
    "inputs",
    "processo",
    "outputs",
    "critérios de qualidade",
    "erros comuns",
)

REQUIRED_MODULE_SECTIONS = (
    "objetivo",
    "quando usar",
    "inputs",
    "processo",
    "outputs",
    "critérios de qualidade",
    "erros comuns",
)

ANSWER_BLOCK_TEMPLATE_SECTIONS = (
    "metadados",
    "intenção e contexto",
    "resposta direta",
    "evidência e suporte",
    "ressalvas e limites",
    "takeaway",
    "revisão de qualidade",
)

ENTITY_MAP_HEADERS = (
    "entity_id",
    "canonical_name",
    "entity_type",
    "definition",
    "aliases",
    "canonical_url",
    "parent_entity_id",
    "relation_type",
    "related_entity_id",
    "locale",
    "evidence_source",
    "evidence_accessed_at",
    "confidence",
    "status",
    "notes",
)

BENCHMARK_HEADERS = (
    "run_id",
    "prompt_id",
    "prompt_version",
    "engine",
    "model_or_surface",
    "web_mode",
    "locale",
    "run_timestamp",
    "iteration",
    "brand",
    "competitors",
    "response_status",
    "brand_present",
    "brand_recommended",
    "target_domain_cited",
    "target_url_cited",
    "citation_support",
    "absorption",
    "entity_accuracy",
    "competitors_present",
    "cited_urls",
    "response_file",
    "evidence_file",
    "reviewer",
    "notes",
)

EVIDENCE_LEDGER_HEADERS = (
    "claim_id",
    "page_url",
    "section",
    "claim",
    "classification",
    "source_url",
    "source_title",
    "source_type",
    "evidence_type",
    "published_at",
    "accessed_at",
    "reliability",
    "confidence",
    "allowed_use",
    "risk",
    "contradiction_status",
    "owner",
    "status",
    "notes",
)

CITATION_OPPORTUNITY_HEADERS = (
    "opportunity_id",
    "page_url",
    "section",
    "claim_without_evidence",
    "evidence_needed",
    "suggested_source_type",
    "suggested_source",
    "priority",
    "risk",
    "owner",
    "status",
    "notes",
)

EXPECTED_BENCHMARK_CRITERIA = (
    "presence",
    "citation",
    "absorption",
    "competitor_comparison",
)


def parse_skill_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Extrai frontmatter YAML e corpo de uma skill."""
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", content, re.DOTALL)
    if not match:
        raise ValueError("frontmatter YAML delimitado por --- não encontrado")

    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter deve ser um objeto YAML")

    return metadata, match.group(2)


def validate_skill(skill_path: Path) -> list[str]:
    """Valida frontmatter, nome e seções obrigatórias de uma skill."""
    errors: list[str] = []

    try:
        content = skill_path.read_text(encoding="utf-8")
        metadata, body = parse_skill_frontmatter(content)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        return [f"{skill_path}: {exc}"]

    name = metadata.get("name")
    description = metadata.get("description")

    if name != skill_path.parent.name:
        errors.append(
            f"{skill_path}: name deve corresponder ao diretório "
            f"'{skill_path.parent.name}'"
        )

    if not isinstance(name, str) or not re.fullmatch(
        r"[a-z0-9]+(?:-[a-z0-9]+)*", name
    ):
        errors.append(f"{skill_path}: name deve usar kebab-case")

    if not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_path}: description é obrigatória")
    elif len(description) > 1024:
        errors.append(f"{skill_path}: description excede 1024 caracteres")

    unexpected_fields = set(metadata) - {"name", "description"}
    if unexpected_fields:
        errors.append(
            f"{skill_path}: frontmatter contém campos não previstos: "
            f"{', '.join(sorted(unexpected_fields))}"
        )

    headings = {
        heading.strip().lower()
        for heading in re.findall(r"^##\s+(.+?)\s*$", body, re.MULTILINE)
    }
    for section in REQUIRED_SKILL_SECTIONS:
        if section not in headings:
            errors.append(f"{skill_path}: seção obrigatória ausente: {section}")

    if "TODO" in body or "[TODO" in content:
        errors.append(f"{skill_path}: contém placeholder TODO")

    return errors


def validate_rubric_data(data: Any, source_name: str) -> list[str]:
    """Valida o contrato de uma rubrica já carregada."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{source_name}: raiz deve ser um objeto YAML"]

    for field in ("id", "name", "version", "scale", "criteria", "interpretation"):
        if field not in data:
            errors.append(f"{source_name}: campo obrigatório ausente: {field}")

    scale = data.get("scale")
    if not isinstance(scale, dict) or scale.get("min") != 0 or scale.get("max") != 4:
        errors.append(f"{source_name}: a escala obrigatória é 0–4")
    elif set(scale.get("labels", {})) != {0, 1, 2, 3, 4}:
        errors.append(f"{source_name}: labels deve definir todos os valores de 0 a 4")

    criteria = data.get("criteria")
    if not isinstance(criteria, list):
        errors.append(f"{source_name}: criteria deve ser uma lista")
        criteria = []

    weights: list[float] = []
    criterion_ids: set[str] = set()
    for index, criterion in enumerate(criteria, start=1):
        prefix = f"{source_name}: critério {index}"
        if not isinstance(criterion, dict):
            errors.append(f"{prefix} deve ser um objeto")
            continue

        for field in ("id", "name", "weight", "evidence_required", "scoring"):
            if field not in criterion:
                errors.append(f"{prefix}: campo obrigatório ausente: {field}")

        criterion_id = criterion.get("id")
        if isinstance(criterion_id, str):
            if criterion_id in criterion_ids:
                errors.append(f"{prefix}: id duplicado: {criterion_id}")
            criterion_ids.add(criterion_id)

        weight = criterion.get("weight")
        if isinstance(weight, (int, float)) and weight > 0:
            weights.append(float(weight))
        else:
            errors.append(f"{prefix}: weight deve ser positivo")

        evidence = criterion.get("evidence_required")
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{prefix}: evidence_required deve conter evidências")

        scoring = criterion.get("scoring")
        if not isinstance(scoring, dict) or not {0, 2, 4}.issubset(scoring):
            errors.append(f"{prefix}: scoring deve definir ao menos 0, 2 e 4")

    if weights and round(sum(weights), 6) not in {1.0, 100.0}:
        errors.append(
            f"{source_name}: pesos devem somar 1.0 ou 100 "
            f"(atual: {sum(weights):g})"
        )

    interpretation = data.get("interpretation")
    if not isinstance(interpretation, list) or not interpretation:
        errors.append(f"{source_name}: interpretation deve conter faixas")

    limitations = data.get("limitations")
    if not isinstance(limitations, list) or not limitations:
        errors.append(f"{source_name}: limitations deve conter limites de uso")

    return errors


def validate_rubric(rubric_path: Path) -> list[str]:
    """Carrega e valida uma rubrica YAML."""
    try:
        data = yaml.safe_load(rubric_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return [f"{rubric_path}: {exc}"]

    return validate_rubric_data(data, str(rubric_path))


def validate_benchmark_data(data: Any, source_name: str) -> list[str]:
    """Valida o contrato do dataset de prompts."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{source_name}: raiz deve ser um objeto JSON"]

    for field in ("schema_version", "locale", "prompts"):
        if field not in data:
            errors.append(f"{source_name}: campo obrigatório ausente: {field}")

    if data.get("locale") != "pt-BR":
        errors.append(f"{source_name}: locale deve ser pt-BR")

    prompts = data.get("prompts")
    if not isinstance(prompts, list) or not prompts:
        errors.append(f"{source_name}: prompts deve ser uma lista não vazia")
        return errors

    prompt_ids: set[str] = set()
    for index, prompt in enumerate(prompts, start=1):
        prefix = f"{source_name}: prompt {index}"
        if not isinstance(prompt, dict):
            errors.append(f"{prefix} deve ser um objeto")
            continue

        for field in (
            "id",
            "prompt",
            "intent",
            "journey_stage",
            "expected_criteria",
        ):
            if field not in prompt:
                errors.append(f"{prefix}: campo obrigatório ausente: {field}")

        prompt_id = prompt.get("id")
        if isinstance(prompt_id, str):
            if prompt_id in prompt_ids:
                errors.append(f"{prefix}: id duplicado: {prompt_id}")
            prompt_ids.add(prompt_id)

        criteria = prompt.get("expected_criteria")
        if not isinstance(criteria, dict):
            errors.append(f"{prefix}: expected_criteria deve ser um objeto")
            continue

        for criterion in EXPECTED_BENCHMARK_CRITERIA:
            value = criteria.get(criterion)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{prefix}: expected_criteria deve definir {criterion}"
                )

    return errors


def validate_benchmark(benchmark_path: Path) -> list[str]:
    """Carrega e valida o dataset de benchmark."""
    try:
        data = json.loads(benchmark_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"{benchmark_path}: {exc}"]

    return validate_benchmark_data(data, str(benchmark_path))


def validate_csv_headers(csv_path: Path, required_headers: list[str] | tuple[str, ...]) -> list[str]:
    """Valida se um template CSV contém os headers exigidos."""
    try:
        with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader, [])
    except (OSError, UnicodeError, csv.Error) as exc:
        return [f"{csv_path}: {exc}"]

    missing = [header for header in required_headers if header not in headers]
    if missing:
        return [
            f"{csv_path}: colunas obrigatórias ausentes: {', '.join(missing)}"
        ]

    if len(headers) != len(set(headers)):
        return [f"{csv_path}: contém colunas duplicadas"]

    return []


def validate_markdown_sections(
    markdown_path: Path,
    required_sections: list[str] | tuple[str, ...],
) -> list[str]:
    """Valida headings de nível 2 em um contrato Markdown."""
    try:
        content = markdown_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{markdown_path}: {exc}"]

    headings = {
        heading.strip().lower()
        for heading in re.findall(r"^##\s+(.+?)\s*$", content, re.MULTILINE)
    }
    errors = [
        f"{markdown_path}: seção obrigatória ausente: {section}"
        for section in required_sections
        if section not in headings
    ]

    if "TODO" in content or "[TODO" in content:
        errors.append(f"{markdown_path}: contém placeholder TODO")

    return errors


def validate_agents_discovery(root: Path) -> list[str]:
    """Valida a camada .agents/skills contra a fonte canônica."""
    errors: list[str] = []
    discovery_root = root / ".agents" / "skills"
    if not discovery_root.exists():
        return [f"{discovery_root}: camada de descoberta ausente"]

    if discovery_root.is_symlink() and discovery_root.resolve() == (root / "skills"):
        return errors

    for skill_name in SKILL_NAMES:
        canonical = root / "skills" / skill_name / "SKILL.md"
        discovered = discovery_root / skill_name / "SKILL.md"
        if not discovered.exists():
            errors.append(f"{discovered}: skill não disponível para descoberta")
            continue

        try:
            canonical_metadata, _ = parse_skill_frontmatter(
                canonical.read_text(encoding="utf-8")
            )
            discovered_content = discovered.read_text(encoding="utf-8")
            discovered_metadata, discovered_body = parse_skill_frontmatter(
                discovered_content
            )
            if canonical_metadata != discovered_metadata:
                errors.append(
                    f"{discovered}: frontmatter diverge da fonte canônica {canonical}"
                )
            canonical_reference = f"../../../skills/{skill_name}/SKILL.md"
            if canonical_reference not in discovered_body:
                errors.append(
                    f"{discovered}: referência canônica ausente: "
                    f"{canonical_reference}"
                )
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{discovered}: {exc}")

    return errors


def validate_repository(root: Path) -> list[str]:
    """Executa todas as validações estruturais do repositório."""
    root = root.resolve()
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"Arquivo obrigatório ausente: {relative_path}")

    if errors:
        return errors

    for skill_name in SKILL_NAMES:
        errors.extend(validate_skill(root / "skills" / skill_name / "SKILL.md"))

    for module_name in (
        "intent-map.md",
        "evidence-ledger.md",
        "answer-blocks.md",
        "citation-engineering.md",
    ):
        errors.extend(
            validate_markdown_sections(
                root / "modules" / module_name,
                REQUIRED_MODULE_SECTIONS,
            )
        )

    for rubric_name in (
        "geo-readiness.yaml",
        "citation-readiness.yaml",
        "entity-authority.yaml",
    ):
        errors.extend(validate_rubric(root / "rubrics" / rubric_name))

    errors.extend(
        validate_benchmark(
            root / "datasets" / "golden" / "benchmark-prompts-pt-br.json"
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "entity-map.csv",
            ENTITY_MAP_HEADERS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "ai-search-benchmark.csv",
            BENCHMARK_HEADERS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "evidence-ledger.csv",
            EVIDENCE_LEDGER_HEADERS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "citation-opportunity-map.csv",
            CITATION_OPPORTUNITY_HEADERS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "answer-block-template.md",
            ANSWER_BLOCK_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(validate_agents_discovery(root))

    agents_content = (root / "AGENTS.md").read_text(encoding="utf-8")
    for marker in ("[FATO]", "[INFERÊNCIA]", "[HIPÓTESE]"):
        if marker not in agents_content:
            errors.append(f"AGENTS.md: marcador obrigatório ausente: {marker}")

    source_ledger = (root / "docs" / "source-ledger.md").read_text(
        encoding="utf-8"
    )
    if "2026-06-21" not in source_ledger:
        errors.append("docs/source-ledger.md: data de acesso inicial ausente")
    if "documentação oficial" not in source_ledger.lower():
        errors.append("docs/source-ledger.md: classificação de fonte oficial ausente")

    return errors


def build_parser() -> argparse.ArgumentParser:
    """Cria o parser da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Valida estrutura, frontmatter, YAML, JSON e CSV do GEO OS."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Raiz do repositório. Padrão: diretório atual.",
    )
    return parser


def main() -> int:
    """Executa a validação e retorna código apropriado."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = build_parser().parse_args()
    errors = validate_repository(args.root)

    if errors:
        print(f"Validação falhou com {len(errors)} erro(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validação concluída: estrutura e contratos estão válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
