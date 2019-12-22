<template>
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      class="demo-ruleForm"
    >
      <p class="title">任务登记表</p>
      <p class="zhu">
          <br>返款时间：</br>
          <br>如有问题请联系客服，如果没有收到返款，请联系表单在线客服或放单的微信。谢谢配合！</br>
      </p>
      <el-form-item label="微信账号" prop="weixin" required>
        <el-input v-model="ruleForm.weixin" placeholder="请填写接单的微信号"></el-input>
      </el-form-item>

      <el-form-item label="手机号" prop="phone" required>
        <el-input v-model="ruleForm.phone" placeholder="请输入本人真实手机号"></el-input>
      </el-form-item>

      <el-form-item label="淘宝旺旺ID" prop="taobao" required>
        <el-input v-model="ruleForm.taobao" placeholder="请填写做单的旺旺ID，不允许换号"></el-input>
      </el-form-item>

       <el-form-item label="地理位置" prop="location" required>
        <el-button type="primary" size="large" class="submit" :loading="load" @click="getLocation">获取地理位置</el-button>
        <el-input type="textarea" v-model="ruleForm.location"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" size="large" class="submit" @click="submitForm('ruleForm')">提交</el-button>
      </el-form-item>
    </el-form>
</template>
<script>
import headTop from "../components/headTop";
import {axios,baseUrl} from "../api/api";
import { location } from "../location";
import qs from 'qs'

export default {
  data() {
    return {
      load: false,
      ruleForm: {
        weixin: "",
        location: "",
        phone: "",
        taobao: "",
      },
      rules: {
        weixin: [
          { required: true, message: "请填写接单的微信号", trigger: "blur" },
        ],
        phone: [
          { required: true, message: "请输入本人真实手机号", trigger: "blur" }
        ],
        taobao: [
           { required: true, message: "请填写做单的旺旺ID，不允许换号", trigger: "blur" }
        ]
      }
    };
  },

  methods: {
     getLocation() {
      console.log("this.load....",this.load)
      this.load = true
      console.log("this.load....11",this.load)
      let _that = this;
      let geolocation = location.initMap("map-container"); //定位
      console.log('get location...')
      console.log(geolocation)
      geolocation.getCurrentPosition(function(status,result){
            if(status=='complete'){
                _that.load = false
                console.log('1111111223wxx')
                console.log(result.position)
                console.log(result.accuracy)
                console.log(result.location_type)
                console.log(result.message)
                console.log(result.addressComponent)
                console.log(result.formattedAddress)
                _that.ruleForm.location = result.formattedAddress
                //_that.ruleForm.location = result.addressComponent
                //console.log(result.accuracy)

            }else{
                _that.load = false
                console.log(7776)
                console.log(result.info)
                console.log(result.message)
                _that.ruleForm.start = result.message
                console.log(556688)
                console.log(_that.ruleForm.start)
                //onError(result)
            }
        })
      //AMap.event.addListener(geolocation, "complete", result => {
       // _that.lat = result.position.lat;
        //_that.lng = result.position.lng;
       // _that.province = result.addressComponent.province;
        //_that.city = result.addressComponent.city;
        //_that.district = result.addressComponent.district;
        //console.log('22222')
        //console.log(_that.lat)
      //});
      //AMap.event.addListener(geolocation, 'complete', onComplete);
      //AMap.event.addListener(geolocation, 'error', onError)
    },
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          console.log('1999...',this.ruleForm.weixin)
          console.log('1998...',this.ruleForm.phone)
          console.log('1997...',this.ruleForm.taobao)
          let params={
            weixin: this.ruleForm.weixin,
            phone: this.ruleForm.phone,
            taobao: this.ruleForm.taobao,
            location: this.ruleForm.location
          };
          axios({
            method: 'post',
            url: baseUrl+'/work/workregister',
            data: qs.stringify(params)
          })
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
             console.log(err)
          })
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>

<style lang="scss" scoped>
.demo-ruleForm{
    box-shadow:0 0 25px #cac6c6;
    //margin: 180 px auto;
    width: 300px;
    padding: 15px 35px 15px 35px;
    //background: blue
    border: 5px solid #cac6c6;
}
.submit{
    width: 300px;
}
.title{
    //color: red;
    //padding: 0px 0px 0px 5px;
    font-size:20px;
}
.zhu{
    color: red;

}

</style>