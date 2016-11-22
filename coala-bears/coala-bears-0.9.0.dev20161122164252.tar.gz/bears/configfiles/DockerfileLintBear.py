import json

from coalib.bearlib.abstractions.Linter import linter
from coalib.bears.requirements.NpmRequirement import NpmRequirement
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY
from coalib.results.Result import Result


@linter(executable='dockerfile_lint')
class DockerfileLintBear:
    """
    Check file syntax as well as arbitrary semantic and best practice
    in Dockerfiles. it also checks LABEL rules against docker images.

    Uses ``dockerfile_lint`` to provide the analysis.
    See <https://github.com/projectatomic/dockerfile_lint#dockerfile-lint> for
    more information .
    """
    LANGUAGES = {"Dockerfile"}
    REQUIREMENTS = {NpmRequirement('dockerfile_lint', '0')}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Syntax', 'Smell'}

    severity_map = {
        "error": RESULT_SEVERITY.MAJOR,
        "warn": RESULT_SEVERITY.NORMAL,
        "info": RESULT_SEVERITY.INFO}

    @staticmethod
    def create_arguments(filename, file, config_file):
        return '--json', '-f', filename

    def process_output(self, output, filename, file):
        output = json.loads(output)

        for severity in output:
            if severity == "summary":
                continue
            for issue in output[severity]["data"]:
                yield Result.from_values(
                    origin=self,
                    message=issue["message"],
                    file=filename,
                    severity=self.severity_map[issue["level"]],
                    line=issue.get("line"))
