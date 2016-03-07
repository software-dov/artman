"""protoc requirements class."""

import subprocess

from pipeline.tasks.requirements import task_requirement_base


class GrpcRequirements(task_requirement_base.TaskRequirementBase):

    @classmethod
    def require(cls):
        """Grpc requires protoc and grpc plugins.

        TODO(cbao): List more grpc plugins.
        TODO(mukai): Take care of the installation of grpc_go_plugin.
        """
        return ['protoc', 'grpc_java_plugin', 'grpc_python_plugin',
                'grpc_go_plugin']

    @classmethod
    def install(cls):
        """Install protoc and grpc plugins via a installation shell script."""
        curl_process = subprocess.Popen(
            ["curl", "-s", "http://goo.gl/getrpc"],
            stdout=subprocess.PIPE)
        bash_process = subprocess.Popen(
            ["bash", "-s", "--"],
            stdin=curl_process.stdout,
            stdout=subprocess.PIPE)
        curl_process.stdout.close()
        return bash_process.communicate()[0]