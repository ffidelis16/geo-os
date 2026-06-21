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
