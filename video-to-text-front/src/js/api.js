// Проверяю ответ сервера
function checkResponse(res) {
    return res.ok ? res.json() : Promise.reject(res.status);
}

class Api {
    constructor({baseUrl, headers}) {
        this._headers = headers;
        this._baseUrl = baseUrl;
    }

    postData(data) {
        return fetch(`${this._baseUrl}`, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        }).then(checkResponse);
    }

    // getData() {
    //   return fetch(`${this._baseUrl}`, {
    //     headers: {
    //       Accept: 'application/json',
    //       'Content-Type': 'application/json',
    //     },
    //   }).then(checkResponse);
    // }
}

export const api = new Api({
    baseUrl: 'http://localhost:5000/api/',
    headers: {},
});
