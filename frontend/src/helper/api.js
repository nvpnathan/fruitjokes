function apiUrl() {
  return 'http://localhost:8000/';
}

export function postApi(pathToResource, data) {
  return fetch(apiUrl() + pathToResource, {
    method: 'POST',
    mode: 'cors',
    body: new URLSearchParams(data),
  });
}
