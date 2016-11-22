from base64 import b64encode
import json
import pytest
import requests
import requests_mock
from cnrclient.client import CnrClient, DEFAULT_REGISTRY, DEFAULT_PREFIX
import cnrclient


def test_headers_without_auth():
    r = CnrClient()
    assert sorted(r.headers.keys()) == ['Content-Type', 'User-Agent']
    assert r.headers["Content-Type"] == "application/json"
    assert r.headers["User-Agent"] == "cnrpy-cli: %s" % cnrclient.__version__


def test_headers_with_auth():
    r = CnrClient(auth="titi")
    assert sorted(r.headers.keys()) == ["Authorization", 'Content-Type', 'User-Agent']
    assert r.headers["Authorization"] == "titi"
    assert r.headers["Content-Type"] == "application/json"
    assert r.headers["User-Agent"] == "cnrpy-cli: %s" % cnrclient.__version__


def test_default_endpoint():
    r = CnrClient(endpoint=None)
    assert r.endpoint.geturl() == DEFAULT_REGISTRY


def test_url():
    r = CnrClient(endpoint="http://test.com")
    assert r._url("/test") == "http://test.com%s/test" % DEFAULT_PREFIX


def test_url_prefix():
    r = CnrClient(endpoint="http://test.com", api_prefix="/test")
    assert r._url("/2") == "http://test.com/test/2"


def test_pull():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = 'package_data'
        m.get(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/orga/p1/1.0.0/helm/pull", text=response)
        assert r.pull("orga/p1", "1.0.0", "helm") == response


def test_pull_discovery_https(discovery_html):
    r = CnrClient()
    with requests_mock.mock() as m:
        response = 'package_data'
        m.get("https://cnr.sh/?cnr-discovery=1", text=discovery_html, complete_qs=True)
        m.get("https://api.kubespray.io/api/v1/packages/orga/p1/pull", text=response)
        assert r.pull("cnr.sh/orga/p1", "1.0.0", "helm") == response


def test_pull_discovery_http(discovery_html):
    r = CnrClient()
    with requests_mock.mock() as m:
        response = 'package_data'
        m.get("https://cnr.sh/?cnr-discovery=1", text="<html/>", complete_qs=True)
        m.get("http://cnr.sh/?cnr-discovery=1", text=discovery_html, complete_qs=True)
        m.get("https://api.kubespray.io/api/v1/packages/orga/p1/pull", text=response)
        assert r.pull("cnr.sh/orga/p1", "1.0.0", "helm") == response


def test_pull_with_version():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = 'package_data'
        m.get(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/orga/p1/1.0.1/helm/pull", complete_qs=True, text=response)
        assert r.pull("orga/p1", "1.0.1", "helm") == response


def test_list_packages():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = '{"packages": "true"}'
        m.get(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages", text=response)
        assert json.dumps(r.list_packages()) == response


def test_list_packages_username():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = '{"packages": "true"}'
        m.get(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages?username=ant31", complete_qs=True, text=response)
        assert json.dumps(r.list_packages(user="ant31")) == response


def test_list_packages_orga():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = '{"packages": "true"}'
        m.get(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages?organization=ant31", complete_qs=True, text=response)
        assert json.dumps(r.list_packages(organization="ant31")) == response


def test_list_packages_orga_and_user():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = '{"packages": "true"}'
        m.get(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages?username=titi&organization=ant31", complete_qs=True, text=response)
        assert json.dumps(r.list_packages(user="titi", organization="ant31")) == response


def test_delete_package():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = '{"packages": "true"}'
        m.delete(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/ant31/kube-ui/1.4.3/helm", complete_qs=True, text=response)
        assert r.delete_package("ant31/kube-ui", "1.4.3", "helm") == {"packages": "true"}


def test_delete_package_version():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = '{"packages": "true"}'
        m.delete(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/ant31/kube-ui/1.4.3/helm", complete_qs=True, text=response)
        assert r.delete_package(name="ant31/kube-ui", version="1.4.3", media_type="helm") == {"packages": "true"}


def test_delete_package_unauthorized():
    r = CnrClient()
    with requests_mock.mock() as m:
        response = '{"packages": "true"}'
        m.delete(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/ant31/kube-ui/1.4.3/helm",
                 complete_qs=True,
                 text=response,
                 status_code=401)
        with pytest.raises(requests.HTTPError):
            r.delete_package("ant31/kube-ui", "1.4.3", "helm")


def test_push_unauthorized():
    r = CnrClient()
    with requests_mock.mock() as m:
        body = {"blob": "fdsfds"}
        response = '{"packages": "true"}'
        m.post(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/ant31/kube-ui?force=false",
               complete_qs=True,
               text=response,
               status_code=401)
        with pytest.raises(requests.HTTPError):
            r.push(name="ant31/kube-ui", body=body)


def test_push():
    body = {"blob": b64encode("testdata")}
    r = CnrClient()
    response = '{"packages": "true"}'
    with requests_mock.mock() as m:
        m.post(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/ant31/kube-ui?force=false",
               complete_qs=True,
               text=response)
        assert json.dumps(r.push(name="ant31/kube-ui", body=body)) == json.dumps(json.loads(response))


def test_push_force():
    body = {"blob": b64encode("foobar")}
    r = CnrClient()
    response = '{"packages": "true"}'
    with requests_mock.mock() as m:
        m.post(DEFAULT_REGISTRY + DEFAULT_PREFIX + "/api/v1/packages/ant31/kube-ui?force=true",
               complete_qs=True,
               text=response)
        assert json.dumps(r.push(name="ant31/kube-ui", body=body, force=True)) == json.dumps(json.loads(response))
