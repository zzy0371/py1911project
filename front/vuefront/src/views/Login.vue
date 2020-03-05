<template>
	<div class="login">
		<label for="">用户名：</label>  <input type="text" v-model="username">
		<br>
		<label for="">密码：</label>  <input type="text" v-model="password">
		<br>
		<button @click="requestToken">发起请求Token</button>
	</div>
	
</template>

<script>
	export default{
		data(){
			return{
				username:"admin",
				password:"123456",
			}  
		},
		methods:{
			requestToken(){
					  this.$api.getToken({
						  username:this.username,
						  password:this.password
					  }).then(res=>{
						  console.log("得到Token",res);
						  this.$jsCookie.set("refresh",res.data.refresh);
						  this.$jsCookie.set("access",res.data.access);
						  this.$router.push("/")
					  }).catch(err=>{
						  console.log("发生错误",err);
					  })
			},
		}
	}
	
</script>

<style>
</style>
