# IN_DATA_DIR="/home/xuwenqiang/flash/SlowFast-main/data/charades/video" #原始视频目录
# OUT_DATA_DIR="/home/xuwenqiang/flash/SlowFast-main/data/charades/frames"         #存放视频帧目录
#IN_DATA_DIR="/home/xuwenqiang/flash/SlowFast-main/data/charades/video" #"/home/xuwenqiang/flash/test"
#OUT_DATA_DIR="/home/xuwenqiang/flash/SlowFast-main/data/charades/frames" #"/home/xuwenqiang/flash/new"
IN_DATA_DIR="/home/xuwenqiang/flash/Charades_v1_480" #"/home/xuwenqiang/flash/test"
OUT_DATA_DIR="/home/xuwenqiang/flash/frames_normal" #"/home/xuwenqiang/flash/new"
if [[ ! -d "${OUT_DATA_DIR}" ]]; then
  echo "${OUT_DATA_DIR} doesn't exist. Creating it.";
  mkdir -p ${OUT_DATA_DIR}
fi

for video in $(find ${IN_DATA_DIR}/ -name *".mp4")
#for video in $(ls -A1 -U ${IN_DATA_DIR}/*)
do
  video_name=${video##*/}

  if [[ $video_name = *".mp4" ]]; then
    video_name=${video_name::-4}
  else
    continue
  fi

  out_video_dir=${OUT_DATA_DIR}/${video_name}/
  mkdir -p "${out_video_dir}"

  out_name="${out_video_dir}/${video_name}-%06d.jpg"

  ffmpeg -i "${video}" -r 30 -q:v 1 "${out_name}"   #ffmpeg -i "${video}" -r 24 -q:v 1 "${out_name}" FTN
done
