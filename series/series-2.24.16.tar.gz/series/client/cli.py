from series.client.errors import SeriesClientException
from series.logging import Logging

from golgi import configurable


@configurable(client=['cli_cmd', 'cli_params'])
class HTTPCLI(Logging):

    def dispatch_command(self, client, cmd_name, params):
        try:
            command = getattr(client, cmd_name)
        except AttributeError:
            self.log.error('No such command: {}'.format(cmd_name))
        else:
            try:
                return command(*params)
            except TypeError as e:
                self.log.error(e)

    def run(self):
        cmd_name = self._cli_cmd[0]
        client = self._client
        try:
            result = self.dispatch_command(client, cmd_name, self._cli_params)
        except SeriesClientException as e:
            self.log.error(e)
        else:
            def err(e):
                self.log.error(e)
                return False
            def succ(m):
                if isinstance(m, str):
                    self.log.info(m)
                else:
                    for l in m:
                        self.log.info(l)
                return True
            return result.cata(err, succ)

    @property
    def _client(self):
        pass

__all__ = ['HTTPCLI']
