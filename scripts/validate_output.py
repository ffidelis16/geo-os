"""Valida a estrutura e os contratos declarativos do GEO OS."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


SKILL_NAMES = (
    "geo-os-orchestrator",
    "geo-diagnosis",
    "entity-map",
    "ai-search-testing",
    "answer-blocks",
    "citation-engineering",
    "content-brief",
    "topical-authority",
    "competitor-analysis",
    "geo-scorecard",
    "extractability-audit",
    "trust-signal-audit",
    "rewrite-plan",
    "content-refresh",
    "schema-opportunity",
)

STRATEGIC_SKILL_NAMES = {
    "content-brief",
    "topical-authority",
    "competitor-analysis",
    "geo-scorecard",
    "extractability-audit",
    "trust-signal-audit",
    "rewrite-plan",
    "content-refresh",
    "schema-opportunity",
}

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "skills/geo-os-orchestrator/SKILL.md",
    ".agents/skills/geo-os-orchestrator/SKILL.md",
    "skills/geo-diagnosis/SKILL.md",
    "skills/entity-map/SKILL.md",
    "skills/ai-search-testing/SKILL.md",
    "skills/answer-blocks/SKILL.md",
    "skills/citation-engineering/SKILL.md",
    "skills/content-brief/SKILL.md",
    "skills/topical-authority/SKILL.md",
    "skills/competitor-analysis/SKILL.md",
    "skills/geo-scorecard/SKILL.md",
    "skills/extractability-audit/SKILL.md",
    "skills/trust-signal-audit/SKILL.md",
    "skills/rewrite-plan/SKILL.md",
    "skills/content-refresh/SKILL.md",
    "skills/schema-opportunity/SKILL.md",
    "modules/intent-map.md",
    "modules/evidence-ledger.md",
    "modules/answer-blocks.md",
    "modules/citation-engineering.md",
    "modules/content-brief.md",
    "modules/topical-authority.md",
    "modules/competitor-analysis.md",
    "modules/geo-scorecard.md",
    "modules/extractability-audit.md",
    "modules/trust-signal-audit.md",
    "modules/rewrite-plan.md",
    "modules/content-refresh.md",
    "modules/schema-opportunity.md",
    "modules/geo-os-orchestrator.md",
    "rubrics/geo-readiness.yaml",
    "rubrics/citation-readiness.yaml",
    "rubrics/entity-authority.yaml",
    "templates/audit-report.md",
    "templates/entity-map.csv",
    "templates/ai-search-benchmark.csv",
    "templates/evidence-ledger.csv",
    "templates/answer-block-template.md",
    "templates/citation-opportunity-map.csv",
    "templates/content-brief-template.md",
    "templates/topical-authority-map.csv",
    "templates/competitor-gap-analysis.csv",
    "templates/geo-scorecard-template.md",
    "templates/geo-scorecard.csv",
    "templates/extractability-audit-template.md",
    "templates/trust-signal-audit-template.md",
    "templates/rewrite-plan-template.md",
    "templates/content-refresh-plan.csv",
    "templates/schema-opportunity-map.csv",
    "templates/optimization-cycle-template.md",
    "templates/workflow-selection-template.md",
    "datasets/golden/benchmark-prompts-pt-br.json",
    "datasets/golden/strategic-planning-prompts-pt-br.json",
    "datasets/golden/evaluation-prompts-pt-br.json",
    "datasets/golden/optimization-prompts-pt-br.json",
    "datasets/golden/orchestrator-prompts-pt-br.json",
    "scripts/validate_output.py",
    "tests/test_validate_output.py",
    "docs/methodology.md",
    "docs/update-policy.md",
    "docs/source-ledger.md",
    "docs/getting-started.md",
    "docs/architecture.md",
    "docs/usage-examples.md",
    "docs/contribution-guide.md",
    "docs/publishing-notes.md",
    "docs/limitations-and-ethics.md",
    "docs/private-overlay.md",
    "examples/sample-geo-audit.md",
    "examples/sample-entity-map.csv",
    "examples/sample-scorecard.md",
    "examples/sample-rewrite-plan.md",
    "examples/sample-optimization-cycle.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/improvement_idea.md",
    ".github/pull_request_template.md",
    "LICENSE",
    "CHANGELOG.md",
    ".gitignore",
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

STRATEGIC_SKILL_SECTIONS = (
    "restrições",
    "modos de falha",
    "exemplo",
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

CONTENT_BRIEF_TEMPLATE_SECTIONS = (
    "metadados",
    "target intent e audiência",
    "estágio de decisão",
    "modelo de entidades",
    "claims e evidências",
    "oportunidades de citação",
    "oportunidades de answer blocks",
    "frescor e qualidade de fontes",
    "links internos",
    "riscos de conteúdo",
    "suposições e limitações",
    "estrutura recomendada",
    "revisão de qualidade",
)

GEO_SCORECARD_TEMPLATE_SECTIONS = (
    "metadados",
    "conteúdo avaliado",
    "contexto, intenção e público",
    "pontuação por dimensão",
    "evidências observadas",
    "lacunas",
    "recomendações e prioridades",
    "limitações",
    "próximos passos",
)

AUDIT_REPORT_TEMPLATE_SECTIONS = (
    "metadados",
    "resumo executivo",
    "perguntas da auditoria",
    "escopo e limitações",
    "evidências",
    "scorecards",
    "diagnóstico",
    "backlog priorizado",
    "plano de teste",
    "riscos",
    "próximas ações",
    "apêndice",
)

EXTRACTABILITY_AUDIT_TEMPLATE_SECTIONS = (
    "metadados",
    "asset e target intent",
    "blocos extraíveis encontrados",
    "blocos ausentes",
    "seções frágeis",
    "oportunidades de answer blocks",
    "oportunidades de schema",
    "recomendações de reestruturação",
    "correções prioritárias",
    "limitações",
)

TRUST_SIGNAL_AUDIT_TEMPLATE_SECTIONS = (
    "metadados",
    "asset e contexto",
    "sinais de autor",
    "sinais de organização",
    "qualidade de fontes e evidências",
    "frescor",
    "metodologia",
    "transparência e limitações",
    "consistência factual",
    "riscos de confiança",
    "melhorias recomendadas",
    "limitações da auditoria",
)

REWRITE_PLAN_TEMPLATE_SECTIONS = (
    "contexto",
    "conteúdo avaliado",
    "principais gaps",
    "plano por seção",
    "ações priorizadas",
    "evidências necessárias",
    "riscos",
    "critérios de reavaliação",
)

OPTIMIZATION_CYCLE_TEMPLATE_SECTIONS = (
    "auditoria de origem",
    "gaps priorizados",
    "ações planejadas",
    "critérios de sucesso",
    "reavaliação",
    "decisão",
)

WORKFLOW_SELECTION_TEMPLATE_SECTIONS = (
    "pedido original",
    "tipo de demanda",
    "fluxo selecionado",
    "fluxos descartados",
    "justificativa",
    "skills em ordem",
    "inputs mínimos",
    "inputs faltantes",
    "templates",
    "output path",
    "limitações",
    "comando pronto para execução",
)

README_PUBLIC_SECTIONS = (
    "o que é o geo os",
    "para quem serve",
    "o que o projeto faz",
    "o que o projeto não faz",
    "arquitetura",
    "uso rápido",
    "como usar os templates",
    "limitações e ética",
    "como contribuir",
    "status do projeto",
)

GETTING_STARTED_SECTIONS = (
    "requisitos",
    "início rápido",
    "tour do repositório",
    "primeiro fluxo",
    "validação",
)

ARCHITECTURE_SECTIONS = (
    "princípios",
    "diretórios",
    "fluxo operacional",
    "skills canônicas e proxies",
    "contratos",
    "limites de arquitetura",
)

USAGE_EXAMPLES_SECTIONS = (
    "auditar um conteúdo",
    "criar um mapa de entidades",
    "transformar gaps em plano de otimização",
)

LIMITATIONS_ETHICS_SECTIONS = (
    "campo emergente",
    "variabilidade dos resultados",
    "ausência de garantias",
    "evidência e rastreabilidade",
    "usos proibidos",
    "revisão humana",
)

SAMPLE_AUDIT_SECTIONS = (
    "metadados",
    "escopo",
    "achados",
    "prioridades",
    "limitações",
)

SAMPLE_SCORECARD_SECTIONS = (
    "contexto",
    "pontuação resumida",
    "evidências",
    "principais gaps",
    "limitações",
)

PUBLIC_GITIGNORE_ENTRIES = (
    "private/",
    "sources/",
    "course-materials/",
    "outputs/",
    "exports/",
    "reports/",
    "*.pdf",
    "*.docx",
    "*.pptx",
    "__pycache__/",
    "*.pyc",
    ".venv/",
    "venv/",
    ".DS_Store",
    "Thumbs.db",
)

PUBLIC_ROOT_FILES = {
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    ".gitignore",
}

PUBLIC_EMAIL_ALLOWLIST: frozenset[str] = frozenset()
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

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

TOPICAL_AUTHORITY_HEADERS = (
    "map_id",
    "primary_entity",
    "supporting_entity",
    "relationship_type",
    "topic_or_question",
    "intent",
    "coverage_status",
    "current_url",
    "depth_level",
    "trust_signal",
    "evidence_needed",
    "cluster_opportunity",
    "suggested_internal_link",
    "editorial_priority",
    "owner",
    "status",
    "notes",
)

COMPETITOR_GAP_HEADERS = (
    "comparison_id",
    "topic_or_intent",
    "primary_entity",
    "competitor",
    "competitor_url",
    "entity_coverage",
    "structural_clarity",
    "evidence_quality",
    "citation_readiness",
    "authorship_trust",
    "freshness",
    "content_modularity",
    "answer_blocks",
    "schema_opportunity",
    "exploitable_gap",
    "recommended_action",
    "priority",
    "evidence_source",
    "accessed_at",
    "notes",
)

GEO_SCORECARD_HEADERS = (
    "audit_id",
    "audit_date",
    "page_or_asset",
    "target_intent",
    "primary_entity",
    "intent_alignment_score",
    "entity_clarity_score",
    "entity_relationship_score",
    "evidence_quality_score",
    "citation_readiness_score",
    "answer_block_readiness_score",
    "extractability_score",
    "topical_completeness_score",
    "trust_signal_score",
    "freshness_score",
    "source_transparency_score",
    "structural_clarity_score",
    "schema_opportunity_score",
    "internal_linking_score",
    "limitations_disclosure_score",
    "actionability_score",
    "total_score",
    "priority",
    "main_gap",
    "recommended_action",
    "evidence_reference",
    "limitations",
    "reviewer",
    "notes",
)

CONTENT_REFRESH_HEADERS = (
    "asset",
    "page_or_section",
    "target_intent",
    "observed_gap",
    "refresh_action",
    "evidence_needed",
    "source_needed",
    "impact_estimate",
    "effort_estimate",
    "priority",
    "risk",
    "owner",
    "status",
    "re_evaluation_criteria",
)

SCHEMA_OPPORTUNITY_HEADERS = (
    "asset",
    "page_or_section",
    "schema_type",
    "justification",
    "required_content",
    "required_properties",
    "missing_fields",
    "risk",
    "priority",
    "validation_criteria",
)

EXPECTED_BENCHMARK_CRITERIA = (
    "presence",
    "citation",
    "absorption",
    "competitor_comparison",
)

EXPECTED_STRATEGIC_CRITERIA = (
    "required_outputs",
    "evidence_discipline",
    "entity_relationships",
    "limitations",
    "actionability",
)

EXPECTED_EVALUATION_CRITERIA = (
    "diagnosis",
    "gap_identification",
    "improvement_recommendations",
    "evidence_needed",
    "interpretation_risks",
    "limitations",
    "actionability",
)

EXPECTED_OPTIMIZATION_CRITERIA = (
    "action_conversion",
    "prioritization",
    "evidence_inference_separation",
    "limitations",
    "over_recommendation_risk",
    "re_evaluation_criteria",
)

EXPECTED_ORCHESTRATOR_CRITERIA = (
    "flow_selection",
    "minimal_sufficiency",
    "missing_inputs",
    "skill_validity",
    "template_guidance",
    "limitations",
    "next_command",
)

ORCHESTRATOR_FLOWS = {
    "audit-existing-content",
    "plan-new-content",
    "improve-existing-content",
    "create-entity-map",
    "create-answer-blocks",
    "map-evidence-citations",
    "plan-ai-search-benchmark",
    "prepare-content-refresh",
    "map-schema-opportunity",
    "consult-methodology",
}

ORCHESTRATOR_TEMPLATE_PATHS = {
    "templates/workflow-selection-template.md",
    "templates/audit-report.md",
    "templates/extractability-audit-template.md",
    "templates/trust-signal-audit-template.md",
    "templates/geo-scorecard-template.md",
    "templates/entity-map.csv",
    "templates/evidence-ledger.csv",
    "templates/content-brief-template.md",
    "templates/competitor-gap-analysis.csv",
    "templates/rewrite-plan-template.md",
    "templates/optimization-cycle-template.md",
    "templates/answer-block-template.md",
    "templates/citation-opportunity-map.csv",
    "templates/ai-search-benchmark.csv",
    "templates/content-refresh-plan.csv",
    "templates/schema-opportunity-map.csv",
}

STRATEGIC_MODULES = {
    "content-brief",
    "topical-authority",
    "competitor-analysis",
}

EVALUATION_MODULES = {
    "geo-scorecard",
    "extractability-audit",
    "trust-signal-audit",
}

OPTIMIZATION_MODULES = {
    "rewrite-plan",
    "content-refresh",
    "schema-opportunity",
}


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

    if skill_path.parent.name in STRATEGIC_SKILL_NAMES:
        for section in STRATEGIC_SKILL_SECTIONS:
            if section not in headings:
                errors.append(
                    f"{skill_path}: seção estratégica obrigatória ausente: {section}"
                )

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
        elif any(
            not isinstance(scoring.get(level), str)
            or not scoring.get(level, "").strip()
            for level in (0, 2, 4)
        ):
            errors.append(
                f"{prefix}: âncoras de scoring 0, 2 e 4 não podem ser vazias"
            )

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

    evaluation_layer = data.get("evaluation_layer")
    if evaluation_layer is not None:
        if not isinstance(evaluation_layer, dict):
            errors.append(f"{source_name}: evaluation_layer deve ser um objeto")
        else:
            for field in (
                "audit_questions",
                "positive_signals",
                "negative_signals",
                "action_rules",
            ):
                value = evaluation_layer.get(field)
                if not isinstance(value, list) or not value:
                    errors.append(
                        f"{source_name}: evaluation_layer.{field} "
                        "deve ser uma lista não vazia"
                    )

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


def validate_strategic_prompt_data(data: Any, source_name: str) -> list[str]:
    """Valida cenários qualitativos da camada de planejamento."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{source_name}: raiz deve ser um objeto JSON"]

    for field in ("schema_version", "locale", "prompts"):
        if field not in data:
            errors.append(f"{source_name}: campo obrigatório ausente: {field}")

    if data.get("locale") != "pt-BR":
        errors.append(f"{source_name}: locale deve ser pt-BR")

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        errors.append(f"{source_name}: prompts deve ser uma lista")
        return errors
    if len(prompts) < 6:
        errors.append(f"{source_name}: prompts deve conter ao menos 6 cenários")

    prompt_ids: set[str] = set()
    covered_modules: set[str] = set()
    for index, prompt in enumerate(prompts, start=1):
        prefix = f"{source_name}: prompt {index}"
        if not isinstance(prompt, dict):
            errors.append(f"{prefix} deve ser um objeto")
            continue

        for field in (
            "id",
            "module",
            "prompt",
            "required_inputs",
            "expected_outputs",
            "expected_criteria",
        ):
            if field not in prompt:
                errors.append(f"{prefix}: campo obrigatório ausente: {field}")

        prompt_id = prompt.get("id")
        if isinstance(prompt_id, str):
            if prompt_id in prompt_ids:
                errors.append(f"{prefix}: id duplicado: {prompt_id}")
            prompt_ids.add(prompt_id)

        module = prompt.get("module")
        if module not in STRATEGIC_MODULES:
            errors.append(f"{prefix}: module inválido: {module}")
        else:
            covered_modules.add(module)

        required_inputs = prompt.get("required_inputs")
        if not isinstance(required_inputs, list) or not required_inputs:
            errors.append(f"{prefix}: required_inputs deve ser uma lista não vazia")

        expected_outputs = prompt.get("expected_outputs")
        if not isinstance(expected_outputs, list) or not expected_outputs:
            errors.append(f"{prefix}: expected_outputs deve ser uma lista não vazia")

        criteria = prompt.get("expected_criteria")
        if not isinstance(criteria, dict):
            errors.append(f"{prefix}: expected_criteria deve ser um objeto")
            continue

        for criterion in EXPECTED_STRATEGIC_CRITERIA:
            value = criteria.get(criterion)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{prefix}: expected_criteria deve definir {criterion}"
                )

    missing_modules = STRATEGIC_MODULES - covered_modules
    if missing_modules:
        errors.append(
            f"{source_name}: módulos sem cenário: {', '.join(sorted(missing_modules))}"
        )

    return errors


def validate_strategic_prompts(dataset_path: Path) -> list[str]:
    """Carrega e valida o dataset de planejamento estratégico."""
    try:
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"{dataset_path}: {exc}"]

    return validate_strategic_prompt_data(data, str(dataset_path))


def validate_evaluation_prompt_data(data: Any, source_name: str) -> list[str]:
    """Valida cenários qualitativos da camada de avaliação."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{source_name}: raiz deve ser um objeto JSON"]

    for field in ("schema_version", "locale", "prompts"):
        if field not in data:
            errors.append(f"{source_name}: campo obrigatório ausente: {field}")

    if data.get("locale") != "pt-BR":
        errors.append(f"{source_name}: locale deve ser pt-BR")

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        errors.append(f"{source_name}: prompts deve ser uma lista")
        return errors
    if len(prompts) < 6:
        errors.append(f"{source_name}: prompts deve conter ao menos 6 cenários")

    prompt_ids: set[str] = set()
    covered_modules: set[str] = set()
    for index, prompt in enumerate(prompts, start=1):
        prefix = f"{source_name}: prompt {index}"
        if not isinstance(prompt, dict):
            errors.append(f"{prefix} deve ser um objeto")
            continue

        for field in (
            "id",
            "module",
            "prompt",
            "provided_artifacts",
            "expected_outputs",
            "expected_criteria",
        ):
            if field not in prompt:
                errors.append(f"{prefix}: campo obrigatório ausente: {field}")

        prompt_id = prompt.get("id")
        if isinstance(prompt_id, str):
            if prompt_id in prompt_ids:
                errors.append(f"{prefix}: id duplicado: {prompt_id}")
            prompt_ids.add(prompt_id)

        module = prompt.get("module")
        if module not in EVALUATION_MODULES:
            errors.append(f"{prefix}: module inválido: {module}")
        else:
            covered_modules.add(module)

        provided_artifacts = prompt.get("provided_artifacts")
        if not isinstance(provided_artifacts, list) or not provided_artifacts:
            errors.append(
                f"{prefix}: provided_artifacts deve ser uma lista não vazia"
            )

        expected_outputs = prompt.get("expected_outputs")
        if not isinstance(expected_outputs, list) or not expected_outputs:
            errors.append(f"{prefix}: expected_outputs deve ser uma lista não vazia")

        criteria = prompt.get("expected_criteria")
        if not isinstance(criteria, dict):
            errors.append(f"{prefix}: expected_criteria deve ser um objeto")
            continue

        for criterion in EXPECTED_EVALUATION_CRITERIA:
            value = criteria.get(criterion)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{prefix}: expected_criteria deve definir {criterion}"
                )

    missing_modules = EVALUATION_MODULES - covered_modules
    if missing_modules:
        errors.append(
            f"{source_name}: módulos sem cenário: {', '.join(sorted(missing_modules))}"
        )

    return errors


def validate_evaluation_prompts(dataset_path: Path) -> list[str]:
    """Carrega e valida o dataset da camada de avaliação."""
    try:
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"{dataset_path}: {exc}"]

    return validate_evaluation_prompt_data(data, str(dataset_path))


def validate_optimization_prompt_data(data: Any, source_name: str) -> list[str]:
    """Valida cenários qualitativos da camada de otimização."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{source_name}: raiz deve ser um objeto JSON"]

    for field in ("schema_version", "locale", "prompts"):
        if field not in data:
            errors.append(f"{source_name}: campo obrigatório ausente: {field}")

    if data.get("locale") != "pt-BR":
        errors.append(f"{source_name}: locale deve ser pt-BR")

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        errors.append(f"{source_name}: prompts deve ser uma lista")
        return errors
    if len(prompts) < 6:
        errors.append(f"{source_name}: prompts deve conter ao menos 6 cenários")

    prompt_ids: set[str] = set()
    covered_modules: set[str] = set()
    for index, prompt in enumerate(prompts, start=1):
        prefix = f"{source_name}: prompt {index}"
        if not isinstance(prompt, dict):
            errors.append(f"{prefix} deve ser um objeto")
            continue

        for field in (
            "id",
            "module",
            "prompt",
            "provided_artifacts",
            "expected_outputs",
            "expected_criteria",
        ):
            if field not in prompt:
                errors.append(f"{prefix}: campo obrigatório ausente: {field}")

        prompt_id = prompt.get("id")
        if isinstance(prompt_id, str):
            if prompt_id in prompt_ids:
                errors.append(f"{prefix}: id duplicado: {prompt_id}")
            prompt_ids.add(prompt_id)

        module = prompt.get("module")
        if module not in OPTIMIZATION_MODULES:
            errors.append(f"{prefix}: module inválido: {module}")
        else:
            covered_modules.add(module)

        provided_artifacts = prompt.get("provided_artifacts")
        if not isinstance(provided_artifacts, list) or not provided_artifacts:
            errors.append(
                f"{prefix}: provided_artifacts deve ser uma lista não vazia"
            )

        expected_outputs = prompt.get("expected_outputs")
        if not isinstance(expected_outputs, list) or not expected_outputs:
            errors.append(f"{prefix}: expected_outputs deve ser uma lista não vazia")

        criteria = prompt.get("expected_criteria")
        if not isinstance(criteria, dict):
            errors.append(f"{prefix}: expected_criteria deve ser um objeto")
            continue

        for criterion in EXPECTED_OPTIMIZATION_CRITERIA:
            value = criteria.get(criterion)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{prefix}: expected_criteria deve definir {criterion}"
                )

    missing_modules = OPTIMIZATION_MODULES - covered_modules
    if missing_modules:
        errors.append(
            f"{source_name}: módulos sem cenário: {', '.join(sorted(missing_modules))}"
        )

    return errors


def validate_optimization_prompts(dataset_path: Path) -> list[str]:
    """Carrega e valida o dataset da camada de otimização."""
    try:
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"{dataset_path}: {exc}"]

    return validate_optimization_prompt_data(data, str(dataset_path))


def validate_orchestrator_prompt_data(data: Any, source_name: str) -> list[str]:
    """Valida cenários qualitativos de roteamento do orquestrador."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{source_name}: raiz deve ser um objeto JSON"]

    for field in ("schema_version", "locale", "prompts"):
        if field not in data:
            errors.append(f"{source_name}: campo obrigatório ausente: {field}")

    if data.get("locale") != "pt-BR":
        errors.append(f"{source_name}: locale deve ser pt-BR")

    prompts = data.get("prompts")
    if not isinstance(prompts, list):
        errors.append(f"{source_name}: prompts deve ser uma lista")
        return errors
    if len(prompts) < 10:
        errors.append(f"{source_name}: prompts deve conter ao menos 10 cenários")

    prompt_ids: set[str] = set()
    covered_flows: set[str] = set()
    worker_skills = set(SKILL_NAMES) - {"geo-os-orchestrator"}

    for index, prompt in enumerate(prompts, start=1):
        prefix = f"{source_name}: prompt {index}"
        if not isinstance(prompt, dict):
            errors.append(f"{prefix} deve ser um objeto")
            continue

        for field in (
            "id",
            "flow",
            "prompt",
            "provided_inputs",
            "expected_skills",
            "expected_templates",
            "expected_criteria",
        ):
            if field not in prompt:
                errors.append(f"{prefix}: campo obrigatório ausente: {field}")

        prompt_id = prompt.get("id")
        if isinstance(prompt_id, str):
            if prompt_id in prompt_ids:
                errors.append(f"{prefix}: id duplicado: {prompt_id}")
            prompt_ids.add(prompt_id)
        else:
            errors.append(f"{prefix}: id deve ser uma string")

        flow = prompt.get("flow")
        if flow not in ORCHESTRATOR_FLOWS:
            errors.append(f"{prefix}: flow inválido: {flow}")
        else:
            covered_flows.add(flow)

        prompt_text = prompt.get("prompt")
        if not isinstance(prompt_text, str) or not prompt_text.strip():
            errors.append(f"{prefix}: prompt deve ser uma string não vazia")

        provided_inputs = prompt.get("provided_inputs")
        if not isinstance(provided_inputs, list):
            errors.append(f"{prefix}: provided_inputs deve ser uma lista")

        expected_skills = prompt.get("expected_skills")
        if not isinstance(expected_skills, list):
            errors.append(f"{prefix}: expected_skills deve ser uma lista")
        else:
            for skill_name in expected_skills:
                if skill_name not in worker_skills:
                    errors.append(f"{prefix}: skill inválida: {skill_name}")

        expected_templates = prompt.get("expected_templates")
        if not isinstance(expected_templates, list) or not expected_templates:
            errors.append(
                f"{prefix}: expected_templates deve ser uma lista não vazia"
            )
        else:
            for template_path in expected_templates:
                if template_path not in ORCHESTRATOR_TEMPLATE_PATHS:
                    errors.append(f"{prefix}: template inválido: {template_path}")

        criteria = prompt.get("expected_criteria")
        if not isinstance(criteria, dict):
            errors.append(f"{prefix}: expected_criteria deve ser um objeto")
            continue

        for criterion in EXPECTED_ORCHESTRATOR_CRITERIA:
            value = criteria.get(criterion)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{prefix}: expected_criteria deve definir {criterion}"
                )

    missing_flows = ORCHESTRATOR_FLOWS - covered_flows
    if missing_flows:
        errors.append(
            f"{source_name}: fluxos sem cenário: {', '.join(sorted(missing_flows))}"
        )

    return errors


def validate_orchestrator_prompts(dataset_path: Path) -> list[str]:
    """Carrega e valida o dataset do orquestrador."""
    try:
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"{dataset_path}: {exc}"]

    return validate_orchestrator_prompt_data(data, str(dataset_path))


def validate_csv_headers(csv_path: Path, required_headers: list[str] | tuple[str, ...]) -> list[str]:
    """Valida se um template CSV contém os headers exigidos."""
    try:
        with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        return [f"{csv_path}: {exc}"]

    headers = rows[0] if rows else []
    errors: list[str] = []
    missing = [header for header in required_headers if header not in headers]
    if missing:
        errors.append(
            f"{csv_path}: colunas obrigatórias ausentes: {', '.join(missing)}"
        )

    if len(headers) != len(set(headers)):
        errors.append(f"{csv_path}: contém colunas duplicadas")

    for line_number, row in enumerate(rows[1:], start=2):
        if not row or not any(cell.strip() for cell in row):
            continue
        if len(row) != len(headers):
            errors.append(
                f"{csv_path}: linha {line_number} possui {len(row)} colunas; "
                f"esperado: {len(headers)}"
            )

    return errors


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


def validate_required_substrings(
    text_path: Path,
    required_values: list[str] | tuple[str, ...],
) -> list[str]:
    """Valida a presença de valores obrigatórios em um arquivo textual."""
    try:
        content = text_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{text_path}: {exc}"]

    return [
        f"{text_path}: valor obrigatório ausente: {value}"
        for value in required_values
        if value not in content
    ]


def _hygiene_candidate_files(root: Path) -> list[Path]:
    """Lista arquivos rastreados e não ignorados, com fallback sem Git."""
    try:
        result = subprocess.run(
            [
                "git",
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
            ],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
    except (OSError, subprocess.SubprocessError, UnicodeError):
        return [path for path in root.rglob("*") if path.is_file()]

    return [
        root / relative
        for line in result.stdout.splitlines()
        if (relative := line.strip())
    ]


def validate_public_hygiene(
    root: Path,
    email_allowlist: set[str] | frozenset[str] | None = None,
) -> list[str]:
    """Detecta caminhos pessoais e materiais privados em áreas públicas."""
    root = root.resolve()
    errors: list[str] = []
    allowed_emails = {
        email.lower()
        for email in (
            PUBLIC_EMAIL_ALLOWLIST if email_allowlist is None else email_allowlist
        )
    }
    personal_path_patterns = (
        re.compile(r"[A-Za-z]:[\\/]+" + "Users" + r"[\\/]+", re.IGNORECASE),
        re.compile("/" + "Users" + r"/[^/\s]+/", re.IGNORECASE),
        re.compile("/" + "home" + r"/[^/\s]+/", re.IGNORECASE),
        re.compile(r"\.codex[\\/]+" + "attachments", re.IGNORECASE),
    )
    private_extensions = {".pdf", ".docx", ".pptx"}
    text_extensions = {
        ".md",
        ".csv",
        ".json",
        ".yaml",
        ".yml",
        ".html",
        ".txt",
        ".py",
    }

    for path in _hygiene_candidate_files(root):
        if not path.is_file():
            continue

        relative = path.relative_to(root)
        if ".git" in relative.parts:
            continue
        if set(relative.parts) & {
            "private",
            "sources",
            "course-materials",
            "outputs",
            "exports",
            "reports",
            "__pycache__",
        }:
            continue

        suffix = path.suffix.lower()
        if suffix in private_extensions:
            errors.append(f"{relative}: material privado não deve ser publicado")
            continue

        lowered_name = path.name.lower()
        if suffix == ".html" and any(
            marker in lowered_name
            for marker in ("apostila", "course-material", "transcript")
        ):
            errors.append(f"{relative}: material de curso não deve ser publicado")

        if suffix not in text_extensions and relative.name not in PUBLIC_ROOT_FILES:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{relative}: {exc}")
            continue

        if any(pattern.search(content) for pattern in personal_path_patterns):
            errors.append(f"{relative}: caminho pessoal encontrado")
        for email in EMAIL_PATTERN.findall(content):
            if email.lower() not in allowed_emails:
                errors.append(f"{relative}: e-mail não allowlistado: {email}")
                break
        if "data:" + "image/" in content.lower():
            errors.append(f"{relative}: imagem base64 incorporada não permitida")

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
        "content-brief.md",
        "topical-authority.md",
        "competitor-analysis.md",
        "geo-scorecard.md",
        "extractability-audit.md",
        "trust-signal-audit.md",
        "rewrite-plan.md",
        "content-refresh.md",
        "schema-opportunity.md",
        "geo-os-orchestrator.md",
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
        validate_strategic_prompts(
            root
            / "datasets"
            / "golden"
            / "strategic-planning-prompts-pt-br.json"
        )
    )
    errors.extend(
        validate_evaluation_prompts(
            root / "datasets" / "golden" / "evaluation-prompts-pt-br.json"
        )
    )
    errors.extend(
        validate_optimization_prompts(
            root / "datasets" / "golden" / "optimization-prompts-pt-br.json"
        )
    )
    errors.extend(
        validate_orchestrator_prompts(
            root / "datasets" / "golden" / "orchestrator-prompts-pt-br.json"
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
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "content-brief-template.md",
            CONTENT_BRIEF_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "topical-authority-map.csv",
            TOPICAL_AUTHORITY_HEADERS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "competitor-gap-analysis.csv",
            COMPETITOR_GAP_HEADERS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "geo-scorecard-template.md",
            GEO_SCORECARD_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "audit-report.md",
            AUDIT_REPORT_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "geo-scorecard.csv",
            GEO_SCORECARD_HEADERS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "extractability-audit-template.md",
            EXTRACTABILITY_AUDIT_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "trust-signal-audit-template.md",
            TRUST_SIGNAL_AUDIT_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "rewrite-plan-template.md",
            REWRITE_PLAN_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "content-refresh-plan.csv",
            CONTENT_REFRESH_HEADERS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "templates" / "schema-opportunity-map.csv",
            SCHEMA_OPPORTUNITY_HEADERS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "optimization-cycle-template.md",
            OPTIMIZATION_CYCLE_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "templates" / "workflow-selection-template.md",
            WORKFLOW_SELECTION_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "README.md",
            README_PUBLIC_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "docs" / "getting-started.md",
            GETTING_STARTED_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "docs" / "architecture.md",
            ARCHITECTURE_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "docs" / "usage-examples.md",
            USAGE_EXAMPLES_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "docs" / "limitations-and-ethics.md",
            LIMITATIONS_ETHICS_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "examples" / "sample-geo-audit.md",
            SAMPLE_AUDIT_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "examples" / "sample-scorecard.md",
            SAMPLE_SCORECARD_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "examples" / "sample-rewrite-plan.md",
            REWRITE_PLAN_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_markdown_sections(
            root / "examples" / "sample-optimization-cycle.md",
            OPTIMIZATION_CYCLE_TEMPLATE_SECTIONS,
        )
    )
    errors.extend(
        validate_csv_headers(
            root / "examples" / "sample-entity-map.csv",
            ENTITY_MAP_HEADERS,
        )
    )
    errors.extend(
        validate_required_substrings(
            root / ".gitignore",
            PUBLIC_GITIGNORE_ENTRIES,
        )
    )
    errors.extend(
        validate_required_substrings(
            root / "LICENSE",
            ("MIT License", "Copyright (c) 2026"),
        )
    )
    errors.extend(validate_public_hygiene(root))
    errors.extend(validate_agents_discovery(root))

    agents_content = (root / "AGENTS.md").read_text(encoding="utf-8")
    for marker in ("[FATO]", "[INFERÊNCIA]", "[HIPÓTESE]", "[RECOMENDAÇÃO]"):
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
        description=(
            "Valida estrutura, frontmatter, YAML, JSON, CSV e higiene pública "
            "do GEO OS."
        )
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
