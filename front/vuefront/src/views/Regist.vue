<template>
	<div class="regist">
	
		<van-form @submit="regist">
		  <van-field
		    v-model="username"
		    name="用户名"
		    label="用户名"
		    placeholder="用户名"
		    :rules="[{ required: true, message: '请填写用户名' }]"
		  />
		  <van-field
		    v-model="password"
		    type="password"
		    name="密码"
		    label="密码"
		    placeholder="密码"
		    :rules="[{ required: true, message: '请填写密码' }]"
		  />
		  <van-field
		    v-model="password2"
		    type="password"
		    name="重复密码"
		    label="重复密码"
		    placeholder="重复密码"
		    :rules="[{ required: true, message: '请填写重复密码' }]"
		  />
		  
		  
		  
		  <div style="margin: 16px;">
		    <van-button round block type="info" native-type="submit">
		      提交
		    </van-button>
		  </div>
		</van-form>
		
		<van-field
		  v-model="telephone"
		  center
		  clearable
		  label="短信验证码"
		  placeholder="请输入短信验证码"
		>
		  <van-button slot="button" size="small" type="primary" @click="sendmsg">发送验证码</van-button>
		</van-field>
		
		<van-field
		  v-model="verify"
		  type="number"
		  name="验证码"
		  label="验证码"
		  placeholder="验证码"
		  :rules="[{ required: true, message: '请填写验证码' }]"
		/>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				username:"",
				password:"",
				password2:"",
				telephone:"",
				verify:""
			}  
		},
		methods:{
			sendmsg(){
				console.log("发送验证码");
				this.$api.sendmsg({
					telephone:this.telephone
				}).then(res=>{
					console.log("发送成功");
				}).catch(err=>{
					发送失败
				})
			},
			regist(){
				this.$api.regist({
					username:this.username,
					password:this.password,
					password2:this.password2
				}).then(res=>{
					this.$router.push("/login/")
				}).catch(err=>{
					this.$toast("注册失败")
				})
			}
		}
	}
</script>

<style>
</style>
