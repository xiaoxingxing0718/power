import Vue from 'vue'
import Router from 'vue-router'
import headTop from '../components/headTop'
import manage from '../page/manage'
import login from '../page/login'
import workregister from '../page/workregister'
import fundlist from '../page/fundData/fundlist'
import plane from '../page/tickets/plane'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: login
    },
    {
      path: '/workregister',
      component: workregister
    },
    {
      path: '/manage',
      component: manage,
      name: 'manage',
      children: [
        {
          path: '',
          component: headTop,
          meta: []
        },
        {
          name: 'fundlist',
          path: 'fundlist',
          component: fundlist,
          meta: ['资金管理', '日常账单']
        },
        {
          name: 'plane',
          path: 'plane',
          component: plane,
          meta: ['票票监控平台', '机票监控']
        }

      ]
    }
  ]
})
