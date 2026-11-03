#!/usr/bin/env python3
"""Inspect the local Renzo-Hacker-Lab project registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "lab.json"


class ManifestError(ValueError):
    """Raised when the lab registry is invalid."""


def load_manifest(path: Path = MANIFEST) -> dict[str, Any]:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ManifestError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ManifestError(f"invalid JSON in {path}: {exc}") from exc

    validate_manifest(manifest)
    return manifest


def validate_manifest(manifest: Any) -> None:
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise ManifestError("manifest must be an object with schema_version 1")

    projects = manifest.get("projects")
    if not isinstance(projects, list):
        raise ManifestError("manifest projects must be a list")

    ids: set[str] = set()
    for project in projects:
        if not isinstance(project, dict):
            raise ManifestError("each project must be an object")
        for field in ("id", "name", "path", "provides"):
            if not isinstance(project.get(field), str) or not project[field]:
                raise ManifestError(f"each project must have a non-empty {field}")
        if project["id"] in ids:
            raise ManifestError(f"duplicate project id: {project['id']}")
        ids.add(project["id"])
        if not isinstance(project.get("runs_alone"), bool):
            raise ManifestError(f"{project['id']}: runs_alone must be a boolean")
        integrations = project.get("integrates_with")
        if not isinstance(integrations, list) or not all(
            isinstance(item, str) for item in integrations
        ):
            raise ManifestError(f"{project['id']}: integrates_with must be a list of ids")

    for project in projects:
        for integration in project["integrates_with"]:
            if integration not in ids:
                raise ManifestError(
                    f"{project['id']}: unknown integration target {integration}"
                )


def project_path(root: Path, relative_path: str) -> Path:
    resolved_root = root.resolve()
    resolved_path = (resolved_root / relative_path).resolve()
    if not resolved_path.is_relative_to(resolved_root):
        raise ManifestError(f"project path escapes workspace: {relative_path}")
    return resolved_path


def print_status(manifest: dict[str, Any], root: Path) -> None:
    print(f"{'PROJECT':<20} {'AVAILABILITY':<13} {'RUNS ALONE':<12} {'PATH'}")
    for project in manifest["projects"]:
        path = project_path(root, project["path"])
        availability = "present" if path.is_dir() else "planned"
        runs_alone = "target" if project["runs_alone"] else "no"
        print(
            f"{project['name']:<20} {availability:<13} {runs_alone:<12} "
            f"{project['path']}"
        )


def print_matrix(manifest: dict[str, Any]) -> None:
    project_width = max(len("PROJECT"), *(len(p["name"]) for p in manifest["projects"]))
    provides_width = max(
        len("PROVIDES"), *(len(p["provides"]) for p in manifest["projects"])
    )
    print(
        f"{'PROJECT':<{project_width}} | {'RUNS ALONE':<12} | "
        f"{'PROVIDES':<{provides_width}} | OPTIONAL INTEGRATIONS"
    )
    for project in manifest["projects"]:
        integrations = ", ".join(project["integrates_with"]) or "—"
        runs_alone = "yes (target)" if project["runs_alone"] else "no"
        print(
            f"{project['name']:<{project_width}} | {runs_alone:<12} | "
            f"{project['provides']:<{provides_width}} | {integrations}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local Renzo-Hacker-Lab orchestrator")
    parser.add_argument(
        "command",
        choices=("status", "matrix", "check"),
        help="show project availability, print the dependency matrix, or validate the registry",
    )
    args = parser.parse_args(argv)

    try:
        manifest = load_manifest()
        if args.command == "status":
            print_status(manifest, ROOT)
        elif args.command == "matrix":
            print_matrix(manifest)
        else:
            present = sum(
                project_path(ROOT, project["path"]).is_dir()
                for project in manifest["projects"]
            )
            total = len(manifest["projects"])
            print(f"Registry valid: {total} projects; {present} paths present.")
    except ManifestError as exc:
        print(f"lab: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
