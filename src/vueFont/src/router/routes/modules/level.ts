import type { AppRouteModule } from '/@/router/types';

import {LAYOUT } from '/@/router/constant';
import { t } from '/@/hooks/web/useI18n';

const permission: AppRouteModule = {
  path: '/main',
  name: 'Level',
  component: LAYOUT,
  redirect: '/level/menu1/menu1-1/menu1-1-1',
  meta: {
    orderNo: 2000,
    icon: 'ion:menu-outline',
    title: t('routes.demo.level.level'),
  },

  children: [
    {
      path: 'upload_music',
      name: 'Menu1Demo',
      component: () => import('/@/views/demo/level/Menu1.vue'),
      meta: {
        title: '音频文件上传或录制',
      },
    },
    {
      path: 'menu2',
      name: 'Menu2Demo',
      component: () => import('/@/views/demo/level/Menu2.vue'),
      meta: {
        title: '生成波型图',
        // ignoreKeepAlive: true,
      },
    },
    {
      path: 'menu3',
      name: '生成语谱图',
      component: () => import('/@/views/demo/level/Menu3.vue'),
      meta: {
        title: '生成语谱图',
        // ignoreKeepAlive: true,
      },
    },
    {
      path: 'menu4',
      name: '语音转文字',
      component: () => import('/@/views/demo/level/Menu4.vue'),
      meta: {
        title: '语音转文字',
        // ignoreKeepAlive: true,
      },
    },
  ],
};

export default permission;
