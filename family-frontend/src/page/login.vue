<template>
  <div class="fill">
    <head-top></head-top>
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="0"
      class="demo-ruleForm"
    >

      <el-form-item label="出发城市" prop="start" required>
        <el-col :span="11">
          <el-input v-model="ruleForm.start"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="到达城市" prop="arrive" required>
        <el-col :span="11">
          <el-input v-model="ruleForm.arrive"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="航程类型" prop="planetype">
        <el-radio-group v-model="ruleForm.planetype">
          <el-radio label="单程"></el-radio>
          <el-radio label="往返"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="出发日期" required>
        <el-col :span="11">
          <el-form-item prop="date1">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="ruleForm.date1"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="返程日期" required>
        <el-col :span="11">
          <el-form-item prop="date2">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="ruleForm.date2"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="平台类型4" prop="type">
        <el-col :span="11">
          <el-checkbox-group v-model="ruleForm.type">
            <el-checkbox label="飞猪" name="type"></el-checkbox>
            <el-checkbox label="京东旅行" name="type"></el-checkbox>
            <el-checkbox label="美团" name="type"></el-checkbox>
            <el-checkbox label="携程" name="type"></el-checkbox>
            <el-checkbox label="去哪儿网" name="type"></el-checkbox>
            <el-checkbox label="途牛" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-col>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import headTop from "../components/headTop";
import {axios,baseUrl} from "../api/api";
import { location } from "../location";

export default {
  data() {
    return {
      ruleForm: {
        start: "",
        arrive: "",
        date1: "",
        date2: "",
        planetype: "",
        type: [],
      },
      rules: {
        start: [
          { required: true, message: "请输入出发城市", trigger: "blur" },
        ],
        arrive: [
          { required: true, message: "请选择到达城市", trigger: "change" }
        ],
        date1: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change"
          }
        ],
        date2: [
          {
            type: "date",
            required: true,
            message: "请选择时间",
            trigger: "change"
          }
        ],
        type: [
          {
            type: "array",
            required: true,
            message: "请至少选择一个平台类型",
            trigger: "change"
          }
        ],
        planetype: [
          { required: true, message: "请选择航程类型", trigger: "change" }
        ]
      }
    };
  },

  mounted() {
    this.getLocation(); // 调用获取地理位置
},

  methods: {
     getLocation() {
      let _that = this;
      let geolocation = location.initMap("map-container"); //定位
      console.log('get location...')
      console.log(geolocation)
      geolocation.getCurrentPosition(function(status,result){
            if(status=='complete'){
                console.log('1111111223wxx')
                console.log(result.position)
                console.log(result.accuracy)
                console.log(result.location_type)
                console.log(result.message)
                console.log(result.addressComponent)
                console.log(result.formattedAddress)
                _that.ruleForm.start = result.message
                //console.log(result.accuracy)

            }else{
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
          console.log('1999...')
          var d1 = this.ruleForm.date1
          var d2 = this.ruleForm.date2
          var depDate =d1.getFullYear() + '-' + (d1.getMonth()+1) + '-' +d1.getDate()
          var arrDate =d2.getFullYear() + '-' + (d2.getMonth()+1) + '-' +d2.getDate()
          //console.log(depDate)
          //alert("submit!");
          axios.get(baseUrl+'/plane/searchAirtickets',{
            params:{
              depCity: this.ruleForm.start,
              arrCity: this.ruleForm.arrive,
              depDate: depDate,
              arrDate: arrDate,
              planetype: this.ruleForm.planetype
            }
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