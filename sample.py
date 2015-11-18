import time
from datetime import datetime

def parse_web(logger, line):
    date, metric_name, metric_value, attrs = line.split('|')
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
    date = time.mktime(date.timetuple())
    metric_name = metric_name.strip()
    metric_value = float(metric_value.strip())
    attr_dict = {}
    for attr_pair in attrs.split(','):
        attr_name, attr_val = attr_pair.split('=')
        attr_name = attr_name.strip()
        attr_val = attr_val.strip()
        attr_dict[attr_name] = attr_val

    return (metric_name, date, metric_value, attr_dict)

def test():
    # Set up the test logger
    import logging
    logging.basicConfig(level=logging.DEBUG)

    # Set up the test input and expected output
    test_input = "Nov 17 11:33:05 vagrant-ubuntu-trusty-64 dd.forwarder[9839]: DEBUG (transaction.py:216): Transaction 132 completed"
    expected = (
        "me.web.requests",
        1320786966,
        157,
        {"metric_type": "counter",
         "unit":        "request" }
    )

    # Call the parse function
    actual = parse_web(logging, test_input)

    # Validate the results
    assert expected == actual, "%s != %s" % (expected, actual)
    print 'test passes'


if __name__ == '__main__':
    # For local testing, callable as "python /path/to/parsers.py"
    test()
