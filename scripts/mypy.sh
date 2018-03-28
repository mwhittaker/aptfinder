#! /usr/bin/env bash

set -euo pipefail

main() {
    mypy aptfinder --ignore-missing-imports
}

main "$@"
