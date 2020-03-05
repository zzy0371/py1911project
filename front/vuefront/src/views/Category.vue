<template>
	<div class="category">
		<van-nav-bar
		  title="分类"
		  left-text="返回"
		  left-arrow
		  @click-left="onClickLeft"
		/>
		这是分类{{$route.params.id}}
		<div v-if="catogory">
			<b>分类ID</b> <span v-text="catogory.id"></span>
			<br>
			<b>分类名字</b> <span v-text="catogory.name"></span>
			
			<ul>
				<li v-for="(item,index) in catogory.goods">  {{item.name}} </li>
				
			</ul>
		</div>
	</div>
</template>

<script>
	export default {
		
		data(){
			return{
				catogory:null
			}
		},
		
		created() {
			this.$api.getCategoryDetail({
				id:this.$route.params.id
			}).then(res=>{
				console.log("分类",res);
				this.catogory = res.data
			}).catch(err=>{
				console.log("出错",err);
			})
		},
		 methods: {
			onClickLeft() {
			  this.$router.go(-1)
			}

		  }
	}
	
	
</script>

<style>
</style>
