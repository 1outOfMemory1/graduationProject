import { defHttp } from '/@/utils/http/axios';


enum Api {
  get_wav_file_list = '/get_wav_file_list',
  get_sound_wave_list = '/get_sound_wave_list',
  get_specgram_pic_url = '/get_specgram_pic_url',
  sound_to_pinyin = '/sound_to_pinyin',
  pinyin_to_text = '/pinyin_to_text',
}


/**
 * @description: get_list_wav_file
 */
export function getWavFileListApi() {
  return defHttp.get({ url: Api.get_wav_file_list }, { errorMessageMode: 'none' });
}


export function getSoundWaveListApi(params) {
  return defHttp.get({ url: Api.get_sound_wave_list,params:params }, { errorMessageMode: 'none' });
}


export function getSpecgramPicUrlApi(params) {
  return defHttp.get({ url: Api.get_specgram_pic_url,params:params }, { errorMessageMode: 'none' });
}

export function soundToPinyin(params) {
  return defHttp.get({ url: Api.sound_to_pinyin,params:params }, { errorMessageMode: 'none' });
}


export function pinyinToText(params) {
  return defHttp.get({ url: Api.pinyin_to_text,params:params }, { errorMessageMode: 'none' });
}
