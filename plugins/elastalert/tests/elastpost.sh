for i in {1..10}; do
  #curl -v -X POST --data '{"Authorization": "blah89d9-blah-blah-blah-blahd3d4blah", "Alert": "<44>Sep  6 21:23:55 SFO01-asasfr SFIMS: [Primary Detection Engine (ef3dbb34-c555-11e4-ba7d-98bb84d7b7c2)][Initial Passive Policy _ sfr01lax02us_corp_auction_local][1:28039:6] \"INDICATOR-COMPROMISE Suspicious .pw dns query\" [Classification: Misc Activity] User: Unknown, Application: Unknown, Client: DNS client, App Protocol: DNS, Interface Ingress: inside, Interface Egress: outside, Security Zone Ingress: N/A, Security Zone Egress: N/A, Context: unknown, [Priority: 3] {UDP} 192.1.21.79:59596 -> 8.8.8.8:53"}' http://127.0.0.1:4444
  curl -v -X POST -H 'Content-Type: application/json' -H 'Accept: application/json;charset=utf-8' -H 'Authorization: Basic dGVzdDo=' -d '{"matches": [{"search": {}, "_id": "0b#kHuAl${(N`QDM1+fW", "_index": "active-logs-000020", "num_hits": 4400, "@timestamp": "2018-02-21T18:28:25.376Z", "lyftlog": {"debug": {}, "errors": {}}, "_type": "syslog", "canary": false, "source": "/var/log/auth.log", "host": "example-staging-iad-000000", "tag": "sshd[4000]:", "asg": "example", "msg": "Did not receive identification string from 127.0.0.1", "num_matches": 4400, "az": "us-east-1a", "region": "iad"}], "rule": "Test"}' http://127.0.0.1:4444
  sleep 1
done

