import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListTask from '@/components/Task/ListTask'
import UpdateTask from '@/components/Task/UpdateTask'
import CreateTask from '@/components/Task/CreateTask'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/tasks',
      name: 'ListTask',
      component: ListTask
    },
    {
      path: '/tasks/:taskId/update',
      name: 'UpdateTask',
      component: UpdateTask
    },
    {
      path: '/tasks/create',
      name: 'CreateTask',
      component: CreateTask
    }
  ],
  mode: 'history'
})
