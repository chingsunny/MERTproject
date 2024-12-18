import numpy as np
import soundfile as sf
import matplotlib as mpl
import matplotlib.pyplot as plt
from pydub import AudioSegment
import glob
#print("我喜歡李泫翰")
dirPath = r"./musicexample/*"
result = glob.glob(dirPath)
for f in result:
    arr = f.split('.')              #./musicexample/test01.mp3
    filetype = 
    musicname = f.split("\\")[1]    #./musicexample\test01.mp3 
    print(f)
    print(musicname)
    if arr[2]=="mp3":
        #mp3 to wav
        sound = AudioSegment.from_mp3(f)
        sound.export("." + arr[1] + ".wav", format="wav")
    # 讀取音訊檔案
    data, samplerate = sf.read("." + arr[1] + ".wav")

    # 將多聲道平均為單聲道
    if data.ndim > 1:
        amp = np.mean(data, axis=1)  
    else:
        amp = data

    # 構建時間軸
    t = np.linspace(0, len(data) / samplerate, num=len(data))

    # 產生繪圖物件
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(15,8))

    # 繪製音頻信號
    #fig, ax1 = plt.subplots()
    ax1.plot(t, data)
    ax1.set_title("Waveform", fontsize=18)
    ax1.set_xlabel("Time [s]", fontsize=14)
    ax1.set_ylabel("Amplitude", fontsize=14)
    ax1.set_ylim(min(amp)*1.3, max(amp)*1.3)

    # 儲存及顯示圖片
    #fig.savefig('Hz_Amplitude.png')
    #fig.show()

    # 構建頻譜圖所需的參數
    Fs = samplerate  # 取樣率
    cmap = "viridis"  # 頻譜圖的顏色映射

    # 創建頻譜圖
    #fig, ax2 = plt.subplots()
    data, freqs, bins, im = ax2.specgram(amp, cmap=cmap, NFFT=1024, Fs=Fs, noverlap=128)
    # 頻譜圖顯示
    ax2.set_title("Spectrogram", fontsize=18)
    ax2.set_xlabel("Time [s]", fontsize=14)
    ax2.set_ylabel("Frequency [Hz]", fontsize=14)
    ax2.set_ylim(0, 22000)

    # 頻譜圖
    cmap = mpl.cm.cool
    Fs = int(1.0 / (t[1]-t[0]))
    fig.suptitle(musicname, fontsize=32)
    fig.colorbar(im, ax=ax2, shrink=0.6, orientation='horizontal', pad=0.2)
    fig.tight_layout(h_pad=2)
    # 儲存及顯示圖片
    fig.savefig("./figure/" + musicname + ".png")
    #fig.show()
