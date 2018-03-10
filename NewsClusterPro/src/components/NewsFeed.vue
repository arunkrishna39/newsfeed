<template>
<el-row :gutter="20">
<el-col :span="6" v-for="(item, index) of newslist" v-bind:key="index">
    <el-card :body-style="{ padding: '0px' }">
      <img v-bind:src="item.image"  class="image">
      <div style="padding: 14px;">
        <p>{{ item.desc }}</p>
        <div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
          <a target="_blank" v-bind:value="item.url" v-bind:href="item.url" title="Manorama"><el-button type="text" class="button">Read More</el-button></a>
        </div>
      </div>
    </el-card>
</el-col>  
</el-row>
</template>
<script>
import axios from 'axios'
export default {
  name: 'newsfeed',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      currentDate: new Date(),
      newslist: [],
      errors: []
    }
  },
  mounted () {
    axios.get('http://localhost:3000/news')
    .then(response => { this.newslist = response.data; console.log(response) })
    .catch(e => { this.errors.push(e); console.log('error', e) })
  }
}
</script>
<style>
  .el-row {
    margin-bottom: 20px;
   }
  .el-col {
    border-radius: 4px;
     margin-bottom: 10px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    margin-bottom: 20px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
    .image {
    width: 100%;
    display: block;
  }
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>
