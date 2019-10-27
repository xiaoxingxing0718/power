<template>
  <div class="fill">
    <head-top></head-top>
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="100px"
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
      <el-form-item label="平台类型" prop="type">
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
import headTop from "../../components/headTop";
import {axios,baseUrl} from "../../api/api";

export default {
  components: {
    headTop
  },

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
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          console.log('1999...')
          //alert("submit!");
          axios.get(baseUrl+'/plane/searchAirtickets',{
            params:{
              name:'wxx'
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