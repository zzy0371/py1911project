<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<div>
		<button @click="requestCategoryList">发起请求分类列表</button>
	</div>
	<div>
		<label for="">用户名：</label>  <input type="text" v-model="username">
		<br>
		<label for="">密码：</label>  <input type="text" v-model="password">
		<br>
		<button @click="requestToken">发起请求Token</button>
	</div>
	
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data(){
	return{
		username:"admin",
		password:"123456"
	}  
  },
  components: {
    // HelloWorld
  },
  methods:{
	  requestCategoryList(){
		  // console.log("点击了按钮");
		  // 获取分类列表
		  this.$http({
			  method:'get',
			  url:'http://127.0.0.1:8000/api/v1/categorys/'
		  }).then(res=>{
			  console.log("得到分类列表",res);
		  }).catch(err=>{
			  console.log("发生错误",err);
		  })
	  },
	  requestToken(){
		  this.$http({
			  method:'post',
			  url:'http://127.0.0.1:8000/obtaintoken/',
			  data:{
				  username:this.username,
				  password:this.password
			  }
		  }).then(res=>{
			  console.log("得到Token",res);
		  }).catch(err=>{
			  console.log("发生错误",err);
		  })
	  }
	  
  }
}
</script>
<!-- 浏览器默认的同源策略不允许跨域访问   域名端口必须一致
Access to XMLHttpRequest 
at 'http://127.0.0.1:8000/api/v1/categorys/' 
from origin 'http://localhost:8080' 
has been blocked by CORS policy: 
No 'Access-Control-Allow-Origin' header is present on the requested resource. -->