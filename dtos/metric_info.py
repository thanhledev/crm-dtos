from .port_info import PortInfo
from typing import List, Dict


class MetricInfo(object):
    """
    Define structure of the information of a tuple job-hostname-endpoint(ip_address:port)
    of worker that defines a single metric exporter's endpoint.
    """

    def __init__(self, hostname: str, inet_addr: str, ports: List[PortInfo]):
        self.hostname = hostname
        self.inet_addr = inet_addr
        self.ports = ports

    def __str__(self):
        return "{}[{}] - ports: {}".format(self.hostname,
                                           self.inet_addr,
                                           str(self.ports))

    def __repr__(self):
        return "{}({}[{}] - ports: {})".format(self.__class__.__name__,
                                               self.hostname,
                                               self.inet_addr,
                                               str(self.ports))

    def metric_fqinfo(self) -> List[Dict]:
        metrics = []
        for info in self.ports:
            metrics.append({'job': info.daemon,
                            'hostname': self.hostname,
                            'endpoint': "{}:{}".format(self.inet_addr, info.port)})

        return metrics
