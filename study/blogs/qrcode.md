## iOS Swift 二维码的生产与扫描

##一、生成二维码
#1.步骤分析
首先创建一个二维码滤镜实例CIFilter，name为“CIQRCodeGenerator”，实例的设置为默认，将准备生产二维码的内容转为utf8格式的data，为滤镜添加数据key为“inputMessage”，利用滤镜输出二维码，调整二维码的大小即清晰度不然得到的二维码很模糊，整个过程注意可选值的判断。
在二维码中间添加图片时首先开启图片上下文，UIGraphicsBeginImageContext(UISize)，先将二维码图片画入上下文，然后将头像画入上下文，通过 UIGraphicsGetImageFromCurrentImageContext()获取新的图片，结束上下文
#2.生产二维码
```base
func createQrcode() -> UIImage? {
//1.创建一个二维码滤镜实例(CIFilter)
let filter = CIFilter.init(name: "CIQRCodeGenerator")
// 滤镜恢复默认设置
filter?.setDefaults()

//2.给滤镜添加数据
guard let data = self.urlStr.data(using: String.Encoding.utf8) else {
return nil
}
filter?.setValue(data, forKey: "inputMessage")

//3.生成二维码
guard let ciImg = filter?.outputImage else {
return nil
}

//4.调整清晰度
//创建Transform
let scale = kScreenW / ciImg.extent.width
let transform = CGAffineTransform.init(scaleX: scale, y: scale)
//放大图片
let bigImg = ciImg.applying(transform)

return UIImage.init(ciImage: bigImg)
}
```
![image](https://raw.githubusercontent.com/ly92/images/master/qrcode/1.png)
#3.在二维码中间添加图片
```base
func createQrcodeWithImage() -> UIImage?{
let qrImg = self.createQrcode()
if self.icon != nil && qrImg != nil{
//开启上下文
UIGraphicsBeginImageContext(qrImg!.size)
//把二维码画到上下文
qrImg!.draw(in: CGRect.init(origin: CGPoint.zero, size: qrImg!.size))

//把前景图画到二维码上
let w :CGFloat = 80
self.icon!.draw(in: CGRect.init(x: (qrImg!.size.width - w) * 0.5, y: (qrImg!.size.height - w) * 0.5, width: w, height: w))

//获取新图片
let newImg = UIGraphicsGetImageFromCurrentImageContext()

//关闭上下文
UIGraphicsEndImageContext()

return newImg
}
return qrImg
}
```
![image](https://raw.githubusercontent.com/ly92/images/master/qrcode/2.png)
##二、扫码
#1.步骤分析
首先设置捕捉设备AVCaptureDevice.defaultDevice(withMediaType: AVMediaTypeVideo)，获取设备的输入与输出，使用会话实例将输入与输出结合，设置输出的识别类型，新建预览图层加入到当前图层的第一位，设置自动对焦以及扫描区域，设置完毕后开始扫描
实现设备输出的代理方法func captureOutput(_ captureOutput: AVCaptureOutput!, didOutputMetadataObjects metadataObjects: [Any]!, from connection: AVCaptureConnection!)，播放声音，处理扫描结果
#2.设置扫描设备
```base
//设置扫描设备
func setUPScanDevice() {

//设置捕捉设备

do{
//设置设备的输入输出
let input = try AVCaptureDeviceInput(device:device)
let output = AVCaptureMetadataOutput()
output.setMetadataObjectsDelegate(self, queue: DispatchQueue.main)
//设置会话
let scanSession = AVCaptureSession()
scanSession.canSetSessionPreset(AVCaptureSessionPresetHigh)

if scanSession.canAddInput(input){
scanSession.addInput(input)
}
if scanSession.canAddOutput(output){
scanSession.addOutput(output)
}

//设置扫描类型(二维码和条形码)
output.metadataObjectTypes = [
AVMetadataObjectTypeQRCode,
AVMetadataObjectTypeCode39Code,
AVMetadataObjectTypeCode128Code,
AVMetadataObjectTypeCode39Mod43Code,
AVMetadataObjectTypeEAN13Code,
AVMetadataObjectTypeEAN8Code,
AVMetadataObjectTypeCode93Code
//                AVMetadataObjectTypeFace
]

//预览图层
let scanPreviewLayer = AVCaptureVideoPreviewLayer.init(session: scanSession)
scanPreviewLayer?.videoGravity = AVLayerVideoGravityResizeAspectFill
scanPreviewLayer?.frame = view.layer.bounds
view.layer.insertSublayer(scanPreviewLayer!, at: 0)

//自动对焦
if (device?.isFocusModeSupported(.autoFocus))!{
do {
try input.device.lockForConfiguration()
}catch{}
input.device.focusMode = .autoFocus
input.device.unlockForConfiguration()
}

//设置扫描区域
//            NotificationCenter.default.addObserver(forName: NSNotification.Name.AVCaptureInputPortFormatDescriptionDidChange, object: nil, queue: nil, using: { [weak self] (noti) in
//                output.rectOfInterest = (scanPreviewLayer?.metadataOutputRectOfInterest(for: self!.scanPane.frame))!
//            })

//保存会话
self.scanSession = scanSession

if !scanSession.isRunning{
scanSession.startRunning()
}

}catch{
//摄像头不可用
LYProgressHUD.showError("相机不可用")
self.navigationController?.popViewController(animated: true)
}
}
```
#3.处理扫描结果
```base
func captureOutput(_ captureOutput: AVCaptureOutput!, didOutputMetadataObjects metadataObjects: [Any]!, from connection: AVCaptureConnection!) {
//停止扫描
self.scanSession.stopRunning()

//建立的SystemSoundID对象
var soundID:SystemSoundID = 0
//获取声音地址
let path = Bundle.main.path(forResource: "scansound", ofType: "wav")
//地址转换
let baseURL = NSURL(fileURLWithPath: path!)
//赋值
AudioServicesCreateSystemSoundID(baseURL, &soundID)
//提醒
AudioServicesPlaySystemSound(soundID)

//扫描结果
if metadataObjects.count > 0{
if let resultObj = metadataObjects.first as? AVMetadataMachineReadableCodeObject{
if self.scanResultBlock != nil{
self.scanResultBlock!(resultObj.stringValue)
self.navigationController?.popViewController(animated: true)
}
}
}
}
```
#4.其他设备操作
```base
//亮灯
do{
try device?.lockForConfiguration()
device?.torchMode = AVCaptureTorchMode.on
device?.flashMode = AVCaptureFlashMode.on
device?.unlockForConfiguration()
}catch{

}

//关灯
do{
try device?.lockForConfiguration()
device?.torchMode = AVCaptureTorchMode.off
device?.flashMode = AVCaptureFlashMode.off
device?.unlockForConfiguration()
}catch{

}
```
![image](https://raw.githubusercontent.com/ly92/images/master/qrcode/3.png)


##三、整体代码---专为懒人和小白添加
```base
import UIKit

class CreateQrcodeView: UIView {

var animateFrame : CGRect = CGRect.init(x: 0, y: 0, width: kScreenW, height: kScreenH)
var urlStr = ""
var icon : UIImage?

var shareBlock : (() -> Void)?

init(frame:CGRect?,urlStr:String, image:UIImage?) {
self.urlStr = urlStr
self.icon = image
if frame == nil{
self.animateFrame = CGRect.init(x: 0, y: 0, width: kScreenW, height: kScreenH)
super.init(frame: CGRect.init(x: 0, y: 0, width: kScreenW, height: kScreenH))
}else{
self.animateFrame = frame!
super.init(frame: frame!)
}
self.setUpUI()
}

required init?(coder aDecoder: NSCoder) {
fatalError("init(coder:) has not been implemented")
}

func setUpUI() {
let bgBtn = UIButton(frame:self.bounds)
bgBtn.backgroundColor = UIColor.RGBSA(s: 0, a: 0.3)
bgBtn.addTarget(self, action: #selector(CreateQrcodeView.hide), for: .touchUpInside)
self.addSubview(bgBtn)

let centerView = UIView()
centerView.x = self.w / 5.0
centerView.w = self.w * 3 / 5.0
centerView.h = centerView.w + 80
centerView.y = (self.h - centerView.h) / 2.0
centerView.backgroundColor = UIColor.white
centerView.clipsToBounds = true
centerView.layer.cornerRadius = 5
self.addSubview(centerView)

let shareBtn = UIButton(frame:CGRect.init(x: centerView.w-50, y: 0, width: 50, height: 50))
shareBtn.setImage(#imageLiteral(resourceName: "Share_code"), for: .normal)
shareBtn.addTarget(self, action: #selector(CreateQrcodeView.share), for: .touchUpInside)
centerView.addSubview(shareBtn)

let codeImgV = UIImageView(frame:CGRect.init(x: 30, y: shareBtn.frame.maxY + 5, width: centerView.w - 60, height: centerView.w-60))
codeImgV.image = self.createQrcodeWithImage()
centerView.addSubview(codeImgV)

let titleLbl = UILabel(frame:CGRect.init(x: 10, y: codeImgV.frame.maxY + 20, width: centerView.w - 20, height: 21))
titleLbl.font = UIFont.systemFont(ofSize: 14.0)
titleLbl.textColor = UIColor.colorHex(hex: "111111")
titleLbl.textAlignment = .center
titleLbl.text = "扫二维码，加入七小服"
centerView.addSubview(titleLbl)
}


func createQrcodeWithImage() -> UIImage?{
let qrImg = self.createQrcode()
if self.icon != nil && qrImg != nil{
//开启上下文
UIGraphicsBeginImageContext(qrImg!.size)
//把二维码画到上下文
qrImg!.draw(in: CGRect.init(origin: CGPoint.zero, size: qrImg!.size))

//把前景图画到二维码上
let w :CGFloat = 80
self.icon!.draw(in: CGRect.init(x: (qrImg!.size.width - w) * 0.5, y: (qrImg!.size.height - w) * 0.5, width: w, height: w))

//获取新图片
let newImg = UIGraphicsGetImageFromCurrentImageContext()

//关闭上下文
UIGraphicsEndImageContext()

return newImg
}

return qrImg
}

func createQrcode() -> UIImage? {
//1.创建一个二维码滤镜实例(CIFilter)
let filter = CIFilter.init(name: "CIQRCodeGenerator")
// 滤镜恢复默认设置
filter?.setDefaults()

//2.给滤镜添加数据
guard let data = self.urlStr.data(using: String.Encoding.utf8) else {
return nil
}
filter?.setValue(data, forKey: "inputMessage")

//3.生成二维码
guard let ciImg = filter?.outputImage else {
return nil
}

//4.调整清晰度
//创建Transform
let scale = kScreenW / ciImg.extent.width
let transform = CGAffineTransform.init(scaleX: scale, y: scale)
//放大图片
let bigImg = ciImg.applying(transform)

return UIImage.init(ciImage: bigImg)
}

func show() {
self.frame = CGRect.zero
UIApplication.shared.keyWindow?.addSubview(self)
UIApplication.shared.keyWindow?.bringSubview(toFront: self)
UIView.animate(withDuration: 0.25, animations: {
self.frame = self.animateFrame
})
}

func hide() {
UIView.animate(withDuration: 0.25, animations: {
self.frame = CGRect.zero
}) { (completion) in
self.removeFromSuperview()
}
}

func share() {
//推荐给好友
if (self.shareBlock != nil){
self.shareBlock!()
}
}
}




import UIKit

class ScanActionViewController: BaseViewController {

var scanResultBlock : ((String) -> Void)?


fileprivate var scanSession = AVCaptureSession()
fileprivate var scanPane = UIView()
fileprivate let line = UIImageView.init(image: #imageLiteral(resourceName: "scan_line"))

fileprivate let device = AVCaptureDevice.defaultDevice(withMediaType: AVMediaTypeVideo)


override func viewDidLoad() {
super.viewDidLoad()
//1afa29
//设置扫描框周边
self.setUPAroundView()

//设置扫描设备
self.setUPScanDevice()



//        //超时提示返回
//        DispatchQueue.main.asyncAfter(deadline: DispatchTime.now() + 6) {
//            LYAlertView.show("提示", "扫描超时，是否重新扫描？", "取消", "确定",{
//                if !self.scanSession.isRunning{
//                    self.scanSession.startRunning()
//                }
//            },{
//                self.navigationController?.popViewController(animated: true)
//            })
//        }

}

override func viewWillAppear(_ animated: Bool) {
super.viewWillAppear(animated)
self.navigationController?.setNavigationBarHidden(true, animated: false)
UIApplication.shared.statusBarStyle = .lightContent
}


override func viewWillDisappear(_ animated: Bool) {
super.viewWillDisappear(animated)
self.navigationController?.setNavigationBarHidden(false, animated: false)
UIApplication.shared.statusBarStyle = .default
}



override func didReceiveMemoryWarning() {
super.didReceiveMemoryWarning()
// Dispose of any resources that can be recreated.
}


//设置扫描框周边
func setUPAroundView() {
self.scanPane = UIView(frame:CGRect.init(x: (kScreenW - 200)/2.0, y: kScreenH/2.0 - 100, width: 200, height: 200))
self.scanPane.backgroundColor = UIColor.clear
self.view.addSubview(self.scanPane)
//扫描框
let imgV = UIImageView(frame:self.scanPane.bounds)
imgV.image = #imageLiteral(resourceName: "scanning_bg")
imgV.contentMode = .scaleAspectFill
self.scanPane.addSubview(imgV)

//扫描线
line.frame = CGRect.init(x: 5, y: 0, width: 190, height: 10)
self.scanPane.addSubview(line)
self.lineRoll()

//周边半透明
let topView = UIView(frame:CGRect.init(x: 0, y: 0, width: kScreenW, height: kScreenH/2.0 - 100))
topView.backgroundColor = UIColor.RGBA(r: 0, g: 0, b: 0, a: 0.3)
self.view.addSubview(topView)
let rightView = UIView(frame:CGRect.init(x: (kScreenW - 200)/2.0 + 200, y: kScreenH/2.0 - 100, width: (kScreenW - 200)/2.0, height: 200))
rightView.backgroundColor = UIColor.RGBA(r: 0, g: 0, b: 0, a: 0.3)
self.view.addSubview(rightView)
let bottomView = UIView(frame:CGRect.init(x: 0, y: kScreenH/2.0 + 100, width: kScreenW, height: kScreenH/2.0 - 100))
bottomView.backgroundColor = UIColor.RGBA(r: 0, g: 0, b: 0, a: 0.3)
self.view.addSubview(bottomView)
let leftView = UIView(frame:CGRect.init(x: 0, y: kScreenH/2.0 - 100, width: (kScreenW - 200)/2.0, height: 200))
leftView.backgroundColor = UIColor.RGBA(r: 0, g: 0, b: 0, a: 0.3)
self.view.addSubview(leftView)

//返回按钮
let backBtn = UIButton(frame:CGRect.init(x: 5, y: 25, width: 55, height: 33))
backBtn.setImage(#imageLiteral(resourceName: "back_white"), for: .normal)
backBtn.addTarget(self, action: #selector(ScanActionViewController.backAction), for: .touchUpInside)
self.view.addSubview(backBtn)

//打开闪光灯按钮
let btn = UIButton(frame:CGRect.init(x: kScreenW/2.0 - 50, y: kScreenH - 150, width: 100, height: 100))
btn.setImage(#imageLiteral(resourceName: "torch_off"), for: .normal)
btn.setImage(#imageLiteral(resourceName: "torch_on"), for: .selected)
btn.addTarget(self, action: #selector(ScanActionViewController.btnAction(btn:)), for: .touchUpInside)
self.view.addSubview(btn)

}

//返回
func backAction() {
self.navigationController?.popViewController(animated: true)
}

//打开闪光灯按钮
func btnAction(btn:UIButton) {
btn.isSelected = !btn.isSelected

if btn.isSelected{
//亮灯
do{
try device?.lockForConfiguration()
device?.torchMode = AVCaptureTorchMode.on
device?.flashMode = AVCaptureFlashMode.on
device?.unlockForConfiguration()
}catch{

}
}else{
//关灯
do{
try device?.lockForConfiguration()
device?.torchMode = AVCaptureTorchMode.off
device?.flashMode = AVCaptureFlashMode.off
device?.unlockForConfiguration()
}catch{

}
}
}

//扫描线滚动
func lineRoll() {
if line.y == 190{
UIView.animate(withDuration: 2.5, animations: {
self.line.y = 0
}) { (completion) in
self.lineRoll()
}
}else{
line.y = 0
UIView.animate(withDuration: 2.5, animations: {
self.line.y = 190
}) { (completion) in
self.lineRoll()
}
}

}


//设置扫描设备
func setUPScanDevice() {

//设置捕捉设备

do{
//设置设备的输入输出
let input = try AVCaptureDeviceInput(device:device)
let output = AVCaptureMetadataOutput()
output.setMetadataObjectsDelegate(self, queue: DispatchQueue.main)
//设置会话
let scanSession = AVCaptureSession()
scanSession.canSetSessionPreset(AVCaptureSessionPresetHigh)

if scanSession.canAddInput(input){
scanSession.addInput(input)
}
if scanSession.canAddOutput(output){
scanSession.addOutput(output)
}

//设置扫描类型(二维码和条形码)
output.metadataObjectTypes = [
AVMetadataObjectTypeQRCode,
AVMetadataObjectTypeCode39Code,
AVMetadataObjectTypeCode128Code,
AVMetadataObjectTypeCode39Mod43Code,
AVMetadataObjectTypeEAN13Code,
AVMetadataObjectTypeEAN8Code,
AVMetadataObjectTypeCode93Code
//                AVMetadataObjectTypeFace
]

//预览图层
let scanPreviewLayer = AVCaptureVideoPreviewLayer.init(session: scanSession)
scanPreviewLayer?.videoGravity = AVLayerVideoGravityResizeAspectFill
scanPreviewLayer?.frame = view.layer.bounds
view.layer.insertSublayer(scanPreviewLayer!, at: 0)

//自动对焦
if (device?.isFocusModeSupported(.autoFocus))!{
do {
try input.device.lockForConfiguration()
}catch{}
input.device.focusMode = .autoFocus
input.device.unlockForConfiguration()
}

//设置扫描区域
//            NotificationCenter.default.addObserver(forName: NSNotification.Name.AVCaptureInputPortFormatDescriptionDidChange, object: nil, queue: nil, using: { [weak self] (noti) in
//                output.rectOfInterest = (scanPreviewLayer?.metadataOutputRectOfInterest(for: self!.scanPane.frame))!
//            })

//保存会话
self.scanSession = scanSession

if !scanSession.isRunning{
scanSession.startRunning()
}

}catch{
//摄像头不可用
LYProgressHUD.showError("相机不可用")
self.navigationController?.popViewController(animated: true)
}

}

}


extension ScanActionViewController : AVCaptureMetadataOutputObjectsDelegate{

func captureOutput(_ captureOutput: AVCaptureOutput!, didOutputMetadataObjects metadataObjects: [Any]!, from connection: AVCaptureConnection!) {
//停止扫描
self.scanSession.stopRunning()

//建立的SystemSoundID对象
var soundID:SystemSoundID = 0
//获取声音地址
let path = Bundle.main.path(forResource: "scansound", ofType: "wav")
//地址转换
let baseURL = NSURL(fileURLWithPath: path!)
//赋值
AudioServicesCreateSystemSoundID(baseURL, &soundID)
//提醒
AudioServicesPlaySystemSound(soundID)

//扫描结果
if metadataObjects.count > 0{
if let resultObj = metadataObjects.first as? AVMetadataMachineReadableCodeObject{
if self.scanResultBlock != nil{
self.scanResultBlock!(resultObj.stringValue)
self.navigationController?.popViewController(animated: true)
}
}
}
}
}

```
