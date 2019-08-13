import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000"
});

const onSuccess = res => {
  return res;
};

const onError = err => {
  if (err.response && err.response.status === 401) {
    window.location.href = "/admin/authentication";
  }

  return Promise.reject(err);
};

api.interceptors.response.use(onSuccess, onError);

export default api;
