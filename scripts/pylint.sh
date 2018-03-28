#! /usr/bin/env bash

set -euo pipefail

main() {
    pylint aptfinder --errors-only
}

main "$@"
