import jsCookie from 'js-cookie'

import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:8000';
// 拦截请求
axios.interceptors.request.use(function (config) {
    // 在发起请求之前可以对请求进行处理  其中config就是请求中的config参数
	if(jsCookie.get('access'))
	{
		config.headers.Authorization=`Bearer ${jsCookie.get('access')}`;
	}
	
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });


// 拦截响应
axios.interceptors.response.use(function (response) {
    // Do something with response data
    return response;
  }, function (error) {
    // Do something with response error
	
	if(error.response.status == 401){
		// 此处选择较为简单的直接重新登录  
		// 还可以根据 refresh对access进行刷新  再次重新请求
		console.log("认证失败");
		window.location.href="#/login/"
		jsCookie.remove("access");
		jsCookie.remove("refresh");
	}
	
	
	
    return Promise.reject(error);
  });




export const getCategoryList = ()=>{
	return axios.get("/api/v1/categorys/")
}

export const getCategoryDetail = (param)=>{
	return axios.get(`/api/v1/categorys/${param.id}`)
}

export const createCategory = (param)=>{
	return axios.post("/api/v1/categorys/",param)
}

export const modifyCategory = (param)=>{
	return axios.put(`/api/v1/categorys/${param.id}/`,param)
}





export const getToken = (param)=>{
	return axios.post("/obtaintoken/",param,)
}


