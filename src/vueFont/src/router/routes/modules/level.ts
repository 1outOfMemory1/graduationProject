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
        title: '音频文件分析',
      },
    },
    {
      path: 'menu2',
      name: 'Menu2Demo',
      component: () => import('/@/views/demo/level/Menu2.vue'),
      meta: {
        title: '在线语音转文字',
        // ignoreKeepAlive: true,
      },
    },
  ],
};

export default permission;
