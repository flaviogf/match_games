import axios from 'axios';

import { toast } from 'react-toastify';

const api = axios.create({
  baseURL: 'http://localhost:5000'
});

const onSuccess = (res) => {
  return res;
};

const onError = (err) => {
  if (err && err.response && err.response.status === 400) {
    err.response.data.errors.forEach(toast.error);
  } else if (err && err.response && err.response.status === 401) {
    window.location.href = '/admin/authentication';
  } else {
    toast.error('Unexpected error.');
  }

  return Promise.reject(err);
};

api.interceptors.response.use(onSuccess, onError);

export default api;
