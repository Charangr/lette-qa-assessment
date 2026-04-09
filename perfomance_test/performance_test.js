import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 50,              // 50 concurrent users
  duration: '30s',      // run test for 30 seconds

  thresholds: {
    http_req_duration: ['p(95)<4000'], // 95% under 4s
    http_req_failed: ['rate<0.01'],    // <1% failures
  },
};

export default function () {
  http.get('https://httpbin.org/delay/3');
  sleep(1);
}