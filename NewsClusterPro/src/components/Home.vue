<template>
<div>
    <el-row>
      <el-col :span="24">
        <el-menu theme="dark" default-active="1" class="el-menu-demo" mode="horizontal">
          <el-menu-item index="1">Latest news</el-menu-item>
          <el-menu-item index="2">Orders</el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
    <news></news>
  </div> 
</template>
<script>
import NewsFeed from './NewsFeed'
export default {
  name: 'home',
  components: {
    'news': NewsFeed
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>
