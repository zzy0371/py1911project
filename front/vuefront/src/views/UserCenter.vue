<template>
	<div class="usercenter">
		用户中心
		<div v-if="userinfo">
			用户名: {{userinfo.username}}
			<br>
			注册日期:{{userinfo.date_joined|dataFormat}}
		</div>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				userinfo:null
			}
		},
		created() {
			this.$api.getUserinfo().then(res=>{
				console.log("个人信息",res)
				this.userinfo=res.data;
				this.$jsCookie.set("userinfo",res.data)
			}).catch(err=>{
				console.log("出错了");
			})
		},
		filters:{
			dataFormat(date){
				date = new Date(date)
				console.log(date, typeof(date));
				return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
			}
		}
	}
	
	
</script>

<style>
</style>
