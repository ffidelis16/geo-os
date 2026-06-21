"""Testes do contrato estrutural do GEO OS."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_output.py"

ITERATION_TWO_FILES = {
    "modules/intent-map.md",
    "modules/evidence-ledger.md",
    "modules/answer-blocks.md",
    "modules/citation-engineering.md",
    "templates/evidence-ledger.csv",
    "templates/answer-block-template.md",
    "templates/citation-opportunity-map.csv",
    "skills/answer-blocks/SKILL.md",
    "skills/citation-engineering/SKILL.md",
}

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

MODULE_SECTIONS = (
    "objetivo",
    "quando usar",
    "inputs",
    "processo",
    "outputs",
    "critérios de qualidade",
    "erros comuns",
)

ANSWER_BLOCK_SECTIONS = (
    "metadados",
    "intenção e contexto",
    "resposta direta",
    "evidência e suporte",
    "ressalvas e limites",
    "takeaway",
    "revisão de qualidade",
)

ITERATION_THREE_FILES = {
    "modules/content-brief.md",
    "modules/topical-authority.md",
    "modules/competitor-analysis.md",
    "templates/content-brief-template.md",
    "templates/topical-authority-map.csv",
    "templates/competitor-gap-analysis.csv",
    "skills/content-brief/SKILL.md",
    "skills/topical-authority/SKILL.md",
    "skills/competitor-analysis/SKILL.md",
    "datasets/golden/strategic-planning-prompts-pt-br.json",
}

STRATEGIC_SKILL_SECTIONS = (
    "objetivo",
    "quando usar",
    "quando não usar",
    "inputs",
    "outputs",
    "processo",
    "restrições",
    "critérios de qualidade",
    "modos de falha",
    "exemplo",
)

CONTENT_BRIEF_SECTIONS = (
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

STRATEGIC_PROMPT_CRITERIA = (
    "required_outputs",
    "evidence_discipline",
    "entity_relationships",
    "limitations",
    "actionability",
)

ITERATION_FOUR_FILES = {
    "modules/geo-scorecard.md",
    "modules/extractability-audit.md",
    "modules/trust-signal-audit.md",
    "templates/geo-scorecard-template.md",
    "templates/geo-scorecard.csv",
    "templates/extractability-audit-template.md",
    "templates/trust-signal-audit-template.md",
    "skills/geo-scorecard/SKILL.md",
    "skills/extractability-audit/SKILL.md",
    "skills/trust-signal-audit/SKILL.md",
    "datasets/golden/evaluation-prompts-pt-br.json",
}

GEO_SCORECARD_SECTIONS = (
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

EXTRACTABILITY_AUDIT_SECTIONS = (
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

TRUST_SIGNAL_AUDIT_SECTIONS = (
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

EVALUATION_PROMPT_CRITERIA = (
    "diagnosis",
    "gap_identification",
    "improvement_recommendations",
    "evidence_needed",
    "interpretation_risks",
    "limitations",
    "actionability",
)

ITERATION_FIVE_FILES = {
    "modules/rewrite-plan.md",
    "modules/content-refresh.md",
    "modules/schema-opportunity.md",
    "templates/rewrite-plan-template.md",
    "templates/content-refresh-plan.csv",
    "templates/schema-opportunity-map.csv",
    "templates/optimization-cycle-template.md",
    "skills/rewrite-plan/SKILL.md",
    "skills/content-refresh/SKILL.md",
    "skills/schema-opportunity/SKILL.md",
    "datasets/golden/optimization-prompts-pt-br.json",
}

REWRITE_PLAN_SECTIONS = (
    "contexto",
    "conteúdo avaliado",
    "principais gaps",
    "plano por seção",
    "ações priorizadas",
    "evidências necessárias",
    "riscos",
    "critérios de reavaliação",
)

OPTIMIZATION_CYCLE_SECTIONS = (
    "auditoria de origem",
    "gaps priorizados",
    "ações planejadas",
    "critérios de sucesso",
    "reavaliação",
    "decisão",
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

OPTIMIZATION_PROMPT_CRITERIA = (
    "action_conversion",
    "prioritization",
    "evidence_inference_separation",
    "limitations",
    "over_recommendation_risk",
    "re_evaluation_criteria",
)

PUBLICATION_FILES = {
    "docs/getting-started.md",
    "docs/architecture.md",
    "docs/usage-examples.md",
    "docs/contribution-guide.md",
    "docs/publishing-notes.md",
    "docs/limitations-and-ethics.md",
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
}

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


def load_validator():
    """Carrega o validador diretamente do repositório."""
    spec = importlib.util.spec_from_file_location("validate_output", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Não foi possível carregar scripts/validate_output.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidateOutputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()

    def test_parse_skill_frontmatter_extracts_required_fields(self) -> None:
        content = """---
name: example-skill
description: Use quando for necessário testar uma skill de exemplo.
---

# Example
"""
        metadata, body = self.validator.parse_skill_frontmatter(content)

        self.assertEqual(metadata["name"], "example-skill")
        self.assertIn("Use quando", metadata["description"])
        self.assertIn("# Example", body)

    def test_validate_skill_rejects_name_different_from_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            skill_dir = Path(temp_dir) / "expected-name"
            skill_dir.mkdir()
            skill_path = skill_dir / "SKILL.md"
            skill_path.write_text(
                "---\n"
                "name: wrong-name\n"
                "description: Use quando o nome precisar ser validado.\n"
                "---\n\n"
                "# Skill\n",
                encoding="utf-8",
            )

            errors = self.validator.validate_skill(skill_path)

        self.assertTrue(any("diretório" in error for error in errors))

    def test_validate_rubric_accepts_scale_weights_and_evidence(self) -> None:
        rubric = {
            "id": "sample",
            "name": "Rubrica de exemplo",
            "version": "0.1.0",
            "scale": {
                "min": 0,
                "max": 4,
                "labels": {
                    0: "ausente",
                    1: "fraco",
                    2: "parcial",
                    3: "sólido",
                    4: "forte",
                },
            },
            "criteria": [
                {
                    "id": "criterion",
                    "name": "Critério",
                    "weight": 1.0,
                    "evidence_required": ["Fonte verificável"],
                    "scoring": {0: "Ausente", 2: "Parcial", 4: "Forte"},
                }
            ],
            "interpretation": [{"min": 0, "max": 4, "label": "Base"}],
            "limitations": ["Não substitui análise humana."],
        }

        errors = self.validator.validate_rubric_data(rubric, "sample.yaml")

        self.assertEqual(errors, [])

    def test_validate_rubric_rejects_scale_outside_zero_to_four(self) -> None:
        rubric = {
            "id": "sample",
            "name": "Rubrica",
            "version": "0.1.0",
            "scale": {"min": 0, "max": 5, "labels": {}},
            "criteria": [],
            "interpretation": [],
            "limitations": [],
        }

        errors = self.validator.validate_rubric_data(rubric, "sample.yaml")

        self.assertTrue(any("0–4" in error for error in errors))

    def test_validate_benchmark_requires_behavioral_criteria(self) -> None:
        benchmark = {
            "schema_version": "0.1.0",
            "locale": "pt-BR",
            "prompts": [
                {
                    "id": "prompt-001",
                    "prompt": "Qual solução atende melhor este cenário?",
                    "intent": "comparative",
                    "journey_stage": "consideration",
                    "expected_criteria": {
                        "presence": "Registrar presença.",
                        "citation": "Registrar citações.",
                    },
                }
            ],
        }

        errors = self.validator.validate_benchmark_data(
            benchmark, "benchmark-prompts-pt-br.json"
        )

        self.assertTrue(any("absorption" in error for error in errors))
        self.assertTrue(any("competitor_comparison" in error for error in errors))

    def test_validate_csv_headers_detects_missing_columns(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "entity-map.csv"
            csv_path.write_text("entity_id,canonical_name\n", encoding="utf-8")

            errors = self.validator.validate_csv_headers(
                csv_path,
                ["entity_id", "canonical_name", "entity_type"],
            )

        self.assertTrue(any("entity_type" in error for error in errors))

    def test_validate_csv_headers_detects_row_width_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "contract.csv"
            csv_path.write_text(
                "first,second,third\n"
                "one,two\n",
                encoding="utf-8",
            )

            errors = self.validator.validate_csv_headers(
                csv_path,
                ["first", "second", "third"],
            )

        self.assertTrue(any("linha 2" in error for error in errors))

    def test_validate_markdown_sections_detects_missing_heading(self) -> None:
        validator = getattr(self.validator, "validate_markdown_sections", None)
        self.assertTrue(callable(validator))

        with tempfile.TemporaryDirectory() as temp_dir:
            markdown_path = Path(temp_dir) / "module.md"
            markdown_path.write_text(
                "# Módulo\n\n## Objetivo\n\nConteúdo.\n",
                encoding="utf-8",
            )

            errors = validator(markdown_path, ("objetivo", "processo"))

        self.assertTrue(any("processo" in error for error in errors))

    def test_iteration_two_files_are_required(self) -> None:
        self.assertTrue(
            ITERATION_TWO_FILES.issubset(set(self.validator.REQUIRED_FILES))
        )

    def test_iteration_two_skills_are_registered(self) -> None:
        self.assertTrue(
            {"answer-blocks", "citation-engineering"}.issubset(
                set(self.validator.SKILL_NAMES)
            )
        )

    def test_iteration_two_modules_have_required_sections(self) -> None:
        for module_name in (
            "intent-map.md",
            "evidence-ledger.md",
            "answer-blocks.md",
            "citation-engineering.md",
        ):
            module_path = REPO_ROOT / "modules" / module_name
            self.assertTrue(module_path.is_file(), module_path)
            content = module_path.read_text(encoding="utf-8").lower()
            for section in MODULE_SECTIONS:
                self.assertIn(f"## {section}", content, module_path)

    def test_answer_block_template_has_required_sections(self) -> None:
        template_path = REPO_ROOT / "templates" / "answer-block-template.md"
        self.assertTrue(template_path.is_file(), template_path)
        content = template_path.read_text(encoding="utf-8").lower()

        for section in ANSWER_BLOCK_SECTIONS:
            self.assertIn(f"## {section}", content)

    def test_evidence_ledger_template_has_contract_headers(self) -> None:
        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "templates" / "evidence-ledger.csv",
            EVIDENCE_LEDGER_HEADERS,
        )

        self.assertEqual(errors, [])

    def test_citation_opportunity_template_has_contract_headers(self) -> None:
        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "templates" / "citation-opportunity-map.csv",
            CITATION_OPPORTUNITY_HEADERS,
        )

        self.assertEqual(errors, [])

    def test_iteration_three_files_are_required(self) -> None:
        self.assertTrue(
            ITERATION_THREE_FILES.issubset(set(self.validator.REQUIRED_FILES))
        )

    def test_iteration_three_skills_are_registered(self) -> None:
        self.assertTrue(
            {"content-brief", "topical-authority", "competitor-analysis"}.issubset(
                set(self.validator.SKILL_NAMES)
            )
        )

    def test_iteration_three_modules_have_required_sections(self) -> None:
        for module_name in (
            "content-brief.md",
            "topical-authority.md",
            "competitor-analysis.md",
        ):
            module_path = REPO_ROOT / "modules" / module_name
            self.assertTrue(module_path.is_file(), module_path)
            content = module_path.read_text(encoding="utf-8").lower()
            for section in MODULE_SECTIONS:
                self.assertIn(f"## {section}", content, module_path)

    def test_iteration_three_skills_have_strategic_contract_sections(self) -> None:
        for skill_name in (
            "content-brief",
            "topical-authority",
            "competitor-analysis",
        ):
            skill_path = REPO_ROOT / "skills" / skill_name / "SKILL.md"
            self.assertTrue(skill_path.is_file(), skill_path)
            _, body = self.validator.parse_skill_frontmatter(
                skill_path.read_text(encoding="utf-8")
            )
            headings = body.lower()
            for section in STRATEGIC_SKILL_SECTIONS:
                self.assertIn(f"## {section}", headings, skill_path)

    def test_content_brief_template_has_required_sections(self) -> None:
        template_path = REPO_ROOT / "templates" / "content-brief-template.md"
        self.assertTrue(template_path.is_file(), template_path)
        content = template_path.read_text(encoding="utf-8").lower()

        for section in CONTENT_BRIEF_SECTIONS:
            self.assertIn(f"## {section}", content)

    def test_topical_authority_template_has_contract_headers(self) -> None:
        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "templates" / "topical-authority-map.csv",
            TOPICAL_AUTHORITY_HEADERS,
        )

        self.assertEqual(errors, [])

    def test_competitor_gap_template_has_contract_headers(self) -> None:
        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "templates" / "competitor-gap-analysis.csv",
            COMPETITOR_GAP_HEADERS,
        )

        self.assertEqual(errors, [])

    def test_strategic_prompt_dataset_has_six_qualitative_scenarios(self) -> None:
        dataset_path = (
            REPO_ROOT
            / "datasets"
            / "golden"
            / "strategic-planning-prompts-pt-br.json"
        )
        self.assertTrue(dataset_path.is_file(), dataset_path)
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
        self.assertEqual(data["locale"], "pt-BR")
        self.assertGreaterEqual(len(data["prompts"]), 6)
        modules = {prompt["module"] for prompt in data["prompts"]}
        self.assertEqual(
            modules,
            {"content-brief", "topical-authority", "competitor-analysis"},
        )
        for prompt in data["prompts"]:
            for criterion in STRATEGIC_PROMPT_CRITERIA:
                self.assertIn(criterion, prompt["expected_criteria"])

    def test_validate_strategic_prompts_requires_qualitative_criteria(self) -> None:
        validator = getattr(
            self.validator,
            "validate_strategic_prompt_data",
            None,
        )
        self.assertTrue(callable(validator))
        data = {
            "schema_version": "0.1.0",
            "locale": "pt-BR",
            "prompts": [
                {
                    "id": "STRATEGIC-001",
                    "module": "content-brief",
                    "prompt": "Crie um brief.",
                    "required_inputs": ["intent"],
                    "expected_outputs": ["brief"],
                    "expected_criteria": {
                        "required_outputs": "Entregar brief.",
                        "evidence_discipline": "Não inventar.",
                    },
                }
            ],
        }

        errors = validator(data, "strategic.json")

        self.assertTrue(any("entity_relationships" in error for error in errors))
        self.assertTrue(any("limitations" in error for error in errors))
        self.assertTrue(any("actionability" in error for error in errors))

    def test_iteration_four_files_are_required(self) -> None:
        self.assertTrue(
            ITERATION_FOUR_FILES.issubset(set(self.validator.REQUIRED_FILES))
        )

    def test_iteration_four_skills_are_registered(self) -> None:
        self.assertTrue(
            {
                "geo-scorecard",
                "extractability-audit",
                "trust-signal-audit",
            }.issubset(set(self.validator.SKILL_NAMES))
        )

    def test_iteration_four_modules_have_required_sections(self) -> None:
        for module_name in (
            "geo-scorecard.md",
            "extractability-audit.md",
            "trust-signal-audit.md",
        ):
            module_path = REPO_ROOT / "modules" / module_name
            self.assertTrue(module_path.is_file(), module_path)
            content = module_path.read_text(encoding="utf-8").lower()
            for section in MODULE_SECTIONS:
                self.assertIn(f"## {section}", content, module_path)

    def test_evaluation_templates_have_required_sections(self) -> None:
        contracts = {
            "geo-scorecard-template.md": GEO_SCORECARD_SECTIONS,
            "extractability-audit-template.md": EXTRACTABILITY_AUDIT_SECTIONS,
            "trust-signal-audit-template.md": TRUST_SIGNAL_AUDIT_SECTIONS,
        }
        for template_name, sections in contracts.items():
            template_path = REPO_ROOT / "templates" / template_name
            self.assertTrue(template_path.is_file(), template_path)
            content = template_path.read_text(encoding="utf-8").lower()
            for section in sections:
                self.assertIn(f"## {section}", content, template_path)

    def test_geo_scorecard_csv_has_contract_headers(self) -> None:
        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "templates" / "geo-scorecard.csv",
            GEO_SCORECARD_HEADERS,
        )

        self.assertEqual(errors, [])

    def test_evaluation_prompt_dataset_has_six_scenarios(self) -> None:
        dataset_path = (
            REPO_ROOT / "datasets" / "golden" / "evaluation-prompts-pt-br.json"
        )
        self.assertTrue(dataset_path.is_file(), dataset_path)
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
        self.assertEqual(data["locale"], "pt-BR")
        self.assertGreaterEqual(len(data["prompts"]), 6)
        modules = {prompt["module"] for prompt in data["prompts"]}
        self.assertEqual(
            modules,
            {"geo-scorecard", "extractability-audit", "trust-signal-audit"},
        )
        for prompt in data["prompts"]:
            for criterion in EVALUATION_PROMPT_CRITERIA:
                self.assertIn(criterion, prompt["expected_criteria"])

    def test_transversal_rubrics_include_evaluation_guidance(self) -> None:
        for rubric_name in (
            "geo-readiness.yaml",
            "citation-readiness.yaml",
            "entity-authority.yaml",
        ):
            data = yaml.safe_load(
                (REPO_ROOT / "rubrics" / rubric_name).read_text(encoding="utf-8")
            )
            guidance = data.get("evaluation_layer")
            self.assertIsInstance(guidance, dict, rubric_name)
            self.assertTrue(guidance.get("audit_questions"), rubric_name)
            self.assertTrue(guidance.get("positive_signals"), rubric_name)
            self.assertTrue(guidance.get("negative_signals"), rubric_name)
            self.assertTrue(guidance.get("action_rules"), rubric_name)

    def test_validate_evaluation_prompts_requires_all_criteria(self) -> None:
        validator = getattr(
            self.validator,
            "validate_evaluation_prompt_data",
            None,
        )
        self.assertTrue(callable(validator))
        data = {
            "schema_version": "0.1.0",
            "locale": "pt-BR",
            "prompts": [
                {
                    "id": "EVAL-001",
                    "module": "geo-scorecard",
                    "prompt": "Avalie o conteúdo.",
                    "provided_artifacts": ["content"],
                    "expected_outputs": ["diagnosis"],
                    "expected_criteria": {
                        "diagnosis": "Diagnosticar.",
                        "gap_identification": "Encontrar lacunas.",
                    },
                }
            ],
        }

        errors = validator(data, "evaluation.json")

        self.assertTrue(
            any("improvement_recommendations" in error for error in errors)
        )
        self.assertTrue(any("interpretation_risks" in error for error in errors))
        self.assertTrue(any("actionability" in error for error in errors))

    def test_iteration_five_files_are_required(self) -> None:
        self.assertTrue(
            ITERATION_FIVE_FILES.issubset(set(self.validator.REQUIRED_FILES))
        )

    def test_iteration_five_skills_are_registered(self) -> None:
        self.assertTrue(
            {"rewrite-plan", "content-refresh", "schema-opportunity"}.issubset(
                set(self.validator.SKILL_NAMES)
            )
        )

    def test_iteration_five_skills_have_strategic_contract_sections(self) -> None:
        for skill_name in (
            "rewrite-plan",
            "content-refresh",
            "schema-opportunity",
        ):
            skill_path = REPO_ROOT / "skills" / skill_name / "SKILL.md"
            self.assertTrue(skill_path.is_file(), skill_path)
            _, body = self.validator.parse_skill_frontmatter(
                skill_path.read_text(encoding="utf-8")
            )
            headings = body.lower()
            for section in STRATEGIC_SKILL_SECTIONS:
                self.assertIn(f"## {section}", headings, skill_path)

    def test_iteration_five_modules_have_required_sections(self) -> None:
        for module_name in (
            "rewrite-plan.md",
            "content-refresh.md",
            "schema-opportunity.md",
        ):
            module_path = REPO_ROOT / "modules" / module_name
            self.assertTrue(module_path.is_file(), module_path)
            content = module_path.read_text(encoding="utf-8").lower()
            for section in MODULE_SECTIONS:
                self.assertIn(f"## {section}", content, module_path)

    def test_rewrite_plan_template_has_required_sections(self) -> None:
        template_path = REPO_ROOT / "templates" / "rewrite-plan-template.md"
        self.assertTrue(template_path.is_file(), template_path)
        content = template_path.read_text(encoding="utf-8").lower()

        for section in REWRITE_PLAN_SECTIONS:
            self.assertIn(f"## {section}", content)

    def test_optimization_cycle_template_has_required_sections(self) -> None:
        template_path = (
            REPO_ROOT / "templates" / "optimization-cycle-template.md"
        )
        self.assertTrue(template_path.is_file(), template_path)
        content = template_path.read_text(encoding="utf-8").lower()

        for section in OPTIMIZATION_CYCLE_SECTIONS:
            self.assertIn(f"## {section}", content)

    def test_content_refresh_template_has_contract_headers(self) -> None:
        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "templates" / "content-refresh-plan.csv",
            CONTENT_REFRESH_HEADERS,
        )

        self.assertEqual(errors, [])

    def test_schema_opportunity_template_has_contract_headers(self) -> None:
        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "templates" / "schema-opportunity-map.csv",
            SCHEMA_OPPORTUNITY_HEADERS,
        )

        self.assertEqual(errors, [])

    def test_optimization_prompt_dataset_has_six_scenarios(self) -> None:
        dataset_path = (
            REPO_ROOT / "datasets" / "golden" / "optimization-prompts-pt-br.json"
        )
        self.assertTrue(dataset_path.is_file(), dataset_path)
        data = json.loads(dataset_path.read_text(encoding="utf-8"))
        self.assertEqual(data["locale"], "pt-BR")
        self.assertGreaterEqual(len(data["prompts"]), 6)
        modules = {prompt["module"] for prompt in data["prompts"]}
        self.assertEqual(
            modules,
            {"rewrite-plan", "content-refresh", "schema-opportunity"},
        )
        for prompt in data["prompts"]:
            for criterion in OPTIMIZATION_PROMPT_CRITERIA:
                self.assertIn(criterion, prompt["expected_criteria"])

    def test_validate_optimization_prompts_requires_all_criteria(self) -> None:
        validator = getattr(
            self.validator,
            "validate_optimization_prompt_data",
            None,
        )
        self.assertTrue(callable(validator))
        data = {
            "schema_version": "0.1.0",
            "locale": "pt-BR",
            "prompts": [
                {
                    "id": "OPT-001",
                    "module": "rewrite-plan",
                    "prompt": "Converta os gaps em plano.",
                    "provided_artifacts": ["geo-scorecard"],
                    "expected_outputs": ["rewrite plan"],
                    "expected_criteria": {
                        "action_conversion": "Converter gaps em ações.",
                        "prioritization": "Priorizar ações.",
                    },
                }
            ],
        }

        errors = validator(data, "optimization.json")

        self.assertTrue(
            any("evidence_inference_separation" in error for error in errors)
        )
        self.assertTrue(any("over_recommendation_risk" in error for error in errors))
        self.assertTrue(any("re_evaluation_criteria" in error for error in errors))

    def test_agents_declares_recommendation_marker(self) -> None:
        agents_content = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("[RECOMENDAÇÃO]", agents_content)

    def test_publication_files_are_required(self) -> None:
        self.assertTrue(PUBLICATION_FILES.issubset(set(self.validator.REQUIRED_FILES)))

    def test_readme_has_public_project_contract(self) -> None:
        readme_path = REPO_ROOT / "README.md"
        content = readme_path.read_text(encoding="utf-8").lower()

        for section in README_PUBLIC_SECTIONS:
            self.assertIn(f"## {section}", content)
        self.assertNotIn("delivery layer", content)
        self.assertNotIn("linguagem comercial", content)

    def test_public_docs_have_required_sections(self) -> None:
        contracts = {
            "getting-started.md": GETTING_STARTED_SECTIONS,
            "architecture.md": ARCHITECTURE_SECTIONS,
            "usage-examples.md": USAGE_EXAMPLES_SECTIONS,
            "limitations-and-ethics.md": LIMITATIONS_ETHICS_SECTIONS,
        }
        for document_name, sections in contracts.items():
            document_path = REPO_ROOT / "docs" / document_name
            self.assertTrue(document_path.is_file(), document_path)
            content = document_path.read_text(encoding="utf-8").lower()
            for section in sections:
                self.assertIn(f"## {section}", content, document_path)

    def test_public_examples_have_required_contracts(self) -> None:
        markdown_contracts = {
            "sample-geo-audit.md": SAMPLE_AUDIT_SECTIONS,
            "sample-scorecard.md": SAMPLE_SCORECARD_SECTIONS,
            "sample-rewrite-plan.md": REWRITE_PLAN_SECTIONS,
            "sample-optimization-cycle.md": OPTIMIZATION_CYCLE_SECTIONS,
        }
        for example_name, sections in markdown_contracts.items():
            example_path = REPO_ROOT / "examples" / example_name
            self.assertTrue(example_path.is_file(), example_path)
            content = example_path.read_text(encoding="utf-8").lower()
            for section in sections:
                self.assertIn(f"## {section}", content, example_path)

        errors = self.validator.validate_csv_headers(
            REPO_ROOT / "examples" / "sample-entity-map.csv",
            self.validator.ENTITY_MAP_HEADERS,
        )
        self.assertEqual(errors, [])

    def test_gitignore_protects_private_and_generated_material(self) -> None:
        gitignore = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")

        for entry in PUBLIC_GITIGNORE_ENTRIES:
            self.assertIn(entry, gitignore)

    def test_license_and_changelog_are_public_ready(self) -> None:
        license_content = (REPO_ROOT / "LICENSE").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("MIT License", license_content)
        for iteration in (
            "Inicialização modular",
            "Evidência e answer blocks",
            "Planejamento estratégico",
            "Avaliação",
            "Otimização",
            "Publicação e documentação",
        ):
            self.assertIn(iteration, changelog)

    def test_validate_public_hygiene_rejects_personal_paths(self) -> None:
        validator = getattr(self.validator, "validate_public_hygiene", None)
        self.assertTrue(callable(validator))

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs").mkdir()
            (root / "docs" / "unsafe.md").write_text(
                r"Fonte em C:\Users\example\Downloads\course.pdf",
                encoding="utf-8",
            )

            errors = validator(root)

        self.assertTrue(any("caminho pessoal" in error for error in errors))

    def test_repository_has_no_public_hygiene_violations(self) -> None:
        errors = self.validator.validate_public_hygiene(REPO_ROOT)

        self.assertEqual(errors, [])

    def test_repository_contract_is_valid(self) -> None:
        errors = self.validator.validate_repository(REPO_ROOT)

        self.assertEqual(errors, [])

    def test_cli_returns_success_for_repository(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--root", str(REPO_ROOT)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validação concluída", result.stdout)


if __name__ == "__main__":
    unittest.main()
