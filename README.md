# UFISH-genes2cells

## 1.0 部署环境    
- 主要用到cellpose，cuda，napari，ufish等。     
- 声明：`gene_to_cell_version_7`是商用代码，请勿在互联网上传播。    
- 安装环境    
```bash
conda env create -f ufish_win_0718.yml -n ufish
```

## 2.0 TIF的前处理（主要是为了构建测试集，可直接跳到3.0进行阅读）    
- 2.1 当我们拿到一个tif的时候，在imagej里面分割通道     
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a01.jpg" width="700" />
 
- 2.2 然后在每一张图片进行最大投影    
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a02.jpg" width="700" />
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a03.jpg" width="700" />

- 2.3 这里我选择了其中一张图片，裁剪出ROI，然后进行test       
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a04.jpg" width="700" />

- 2.4 这里我把上述做过的最大投影并且裁剪出来的图片，进行merge    
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a05.jpg" width="700" />
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a06.jpg" width="700" />    

最后得到一个`Composite.tif`的test图片    

## 3.0 UFISH 斑点检测     
- 把图片（5个通道，5号dapi，1-4号目标基因）`Composite.tif`放到`test`文件夹，输出目录在`predict`文件夹，然后运行以下命令，`cyx`的`c`指的是通道。如果图片只有一个通道就改成`yx`       
- win安装的conda，家目录都是类似于这样：`C:\Users\yang`，我们把代码`gene_to_cell_version_7`和图片`test\Composite.tif`都存放在这个路径。     
- 声明：`gene_to_cell_version_7`是商用代码，请勿在互联网上传播。     

执行以下命令进行斑点检测    
```bash
ufish predict-imgs test predict --img_glob="*.tif" --intensity_threshold 0.5 --axes='cyx'    
```
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a07.jpg" width="700" />      

- 3.1 该结果存放于`predict`，使用以下脚本转换csv格式（win）     
```bash
python .\gene_to_cell_version_7\changePred.py .\predict\Composite.pred.csv .\predict\temp.csv
```
- 3.2 使用以下脚本删除dapi通道，例如C4（win）
```bash
python .\gene_to_cell_version_7\remove_gene.py .\predict\temp.csv C4 .\predict\all_gene_location.csv
```
- 3.3 使用以下脚本拆分通道（win）
```bash
python .\gene_to_cell_version_7\split_gene.py .\predict\all_gene_location.csv .\predict\
```
- 3.4 构建以下文件夹存放（win）    
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a08.jpg" width="400" />  <img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a09.jpg" width="400" /> 

## 4.0 cellpose细胞分割    
使用`dapi.tif`进行细胞分割。    
首先点击`calibrate`预估细胞直径，运行完毕，再点击`additional settings`中的`flow threshold`改为5.4，`cellprob threshold`改为-3    
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a10.jpg" width="700" />     

然后`ctrl+s`保存，得到`dapi_seg.npy`    
<img src="https://github.com/y741269430/UFISH-genes2cells/blob/main/Imgs/a11.jpg" width="400" />     

## 5.0 执行genns to cells    
将上述构建好的`raw_data`文件，放在桌面，然后运行：(你可以在`main.py`脚本中，自定义输入路径以及输出路径)    

```bash
python .\gene_to_cell_version_7\main.py
```
完成    
