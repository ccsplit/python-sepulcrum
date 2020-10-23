from ..context import sort_ips


def test_ip_sort():
    result = sort_ips(["192.168.1.1", "34.23.21.1", "243.123.12.12", "12.123.41.12"])
    actual = ["12.123.41.12", "34.23.21.1", "192.168.1.1", "243.123.12.12"]
    assert result == actual, "The sort_ips function did not sort properly."
