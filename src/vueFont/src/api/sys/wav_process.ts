import { defHttp } from '/@/utils/http/axios';


enum Api {
  list_wav_file = '/list_wav_file',
}


/**
 * @description: get_list_wav_file
 */
export function getListWavFileApi() {
  return defHttp.get({ url: Api.list_wav_file }, { errorMessageMode: 'none' });
}
