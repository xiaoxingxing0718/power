<template>
  <div class="fill">
    <head-top></head-top>

    <div class="form">
      <el-form :inline="true" class="demo-form-inline">
        <el-form-item>
          <el-input placeholder="请输入微信账号"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input placeholder="请输入距离(km)"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">计算距离
          </el-button>
        </el-form-item>
        <div class="button">
          <el-button type="primary">新增</el-button>
        </div>
      </el-form>
    </div>

    <el-table :data="tableData" style="width: 100%" max-height="450">
      <el-table-column fixed prop="weixin" label="微信账号" width="150"></el-table-column>
      <el-table-column prop="phone" label="手机号" width="120"></el-table-column>
      <el-table-column prop="taobao" label="淘宝会员名" width="120"></el-table-column>
      <el-table-column prop="location" label="地理位置" width="200"></el-table-column>
      <el-table-column prop="distance" label="距离" width="120"></el-table-column>
      <el-table-column prop="checkweixin" label="审核员微信" width="150"></el-table-column>
      <el-table-column prop="remark" label="备注" width="120"></el-table-column>
      <el-table-column prop="from" label="来源" width="120"></el-table-column>
      <el-table-column prop="checkresult" label="审核结果" width="120"></el-table-column>
      <el-table-column prop="trun" label="交接" width="120"></el-table-column>
      <el-table-column fixed="right" label="操作" width="100">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
          <el-button type="text" size="small">修改</el-button>
          <el-button @click="handleClick(scope.row)" type="text" size="small">计算</el-button>
          <el-button @click.native.prevent="deleteRow(scope.$index, tableData)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import headTop from "../../components/headTop";
export default {
  methods: {
    handleClick(row) {
      console.log(row);
    }
  },

  created() {
    console.log("12344");
  },

  components: {
    headTop
  },

  data() {
    return {
      tableData: [
        {
          weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
          from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",

        },
        {
           weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        },
        {
           weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        },
        {
          weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        },
        {
          weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        },
        {
          weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        },
        {
           weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        },
        {
          weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        },
        {
          weixin: "18482273757",
          phone: "18482273757",
          taobao: "xiaoxinxin",
          location: "上海市普陀区金沙江路 1518 弄",
          distance: "",
          checkweixin: "张三",
          remark: "做单",        
           from: "内部粉丝",
          checkresult: "通过",
          trun: "小猫",
        }
      ]
    };
  },

  methods: {
     deleteRow(index, rows) {
        rows.splice(index, 1);
      }
  }
};
</script>

<style lang="scss">
.fill {
  display: block;
  position: fixed;
  top: 120px;
  width: 950px;
  left: 230px;
}

.form {
  display: block;
  position: fixed;
  top: 70px;
  width: 950px;
  left: 230px;
}

.button{
  display: block;
  position: fixed;
  top: 70px;
  width: 950px;
  left: 1200px;
}
</style>