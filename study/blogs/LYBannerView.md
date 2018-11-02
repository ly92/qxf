利用闲暇时间写了一个banner
## 原理
scrollview中添加3张图片，每次都是显示中间那张图片，当滚动或者按照时间轮播的时候显示后一张的同时将后一张图片放在中间并且scrollview显示中间图片，并重置两边的图片
##问题 
现在用手滚动的时候效果还算满意，但是根据定时器轮播的时候图片总是闪换，无法达到手动滑动的那种顺畅感觉，如果有好的方法请联系我，感谢！

##效果
支持横向轮播和纵向轮播
使用方法，可设置imgUrlArray图片地址数组，customerTitleArray仅显示title，customerImgArray图片数组，也可设置pagecontrol的颜色以及是否隐藏
![image](https://raw.githubusercontent.com/ly92/images/master/LYTools/banner1.png)
![image](https://raw.githubusercontent.com/ly92/images/master/LYTools/banner2.png)
##使用
```base
//横向轮播
lazy var bannerView1 : LYBannerView = {
let bannerView = LYBannerView(frame: CGRect(x: 0, y: 0, width: kScreenW, height: kScreenW * 320 / 750), isHorizontalScroll: true, delegate: self)
bannerView.backgroundColor = UIColor.white
bannerView.currentColor = UIColor.blue
bannerView.normalColor = UIColor.green
bannerView.showPageControl = true
bannerView.tag = 2112
self.headerView.addSubview(bannerView)
return bannerView
}()
//纵向轮播
lazy var bannerView2 : LYBannerView = {
let bannerView = LYBannerView(frame: CGRect(x: 80, y: 0, width: kScreenW - 80 - 60, height: 49), isHorizontalScroll: false, delegate: self)
bannerView.showPageControl = false
bannerView.backgroundColor = UIColor.white
bannerView.tag = 2222
self.recommendView.addSubview(bannerView)
return bannerView
}()

//设置图片url或者显示的title
self.bannerView1.imgUrlArray = bannerArray3
self.bannerView2.customerTitleArray = bannerArray4
```

##源码
```base
//
//  LYBannerView.swift
//  qixiaofu
//   _
//  | |      /\   /\
//  | |      \ \_/ /
//  | |       \_~_/
//  | |        / \
//  | |__/\    [ ]
//  |_|__,/    \_/
//
//  Created by ly on 2017/6/15.
//  Copyright © 2017年 qixiaofu. All rights reserved.
//

import UIKit

@objc
protocol LYBannerViewDelegate : NSObjectProtocol {
@objc func lyBannerClick(lyBanner:LYBannerView, index : Int)
}

class LYBannerView: UIView {

var delegate : LYBannerViewDelegate?

var currentColor : UIColor{//当前page的颜色
didSet{
self.pageControl.currentPageIndicatorTintColor = currentColor
}
}
var normalColor : UIColor{//其他page的颜色
didSet{
self.pageControl.pageIndicatorTintColor = normalColor
}
}
var showPageControl : Bool{//是否显示页码控制器
didSet{
if !showPageControl {
self.pageControl.isHidden = true
}
}
}

var customerImgArray : Array<UIImage>{//显示的图片后期赋值
didSet{
self.imgArray = customerImgArray
self.setUpSubviews()
}
}
var customerTitleArray : Array<String>{//显示的标题后期赋值
didSet{
self.imgArray = self.convertStringArrayToImageArray(stringArray: customerTitleArray)
self.setUpSubviews()
}
}
var imgUrlArray : Array<String>{//显示图片的地址后期赋值
didSet{
self.isUrl = true
self.setUpSubviews()
}
}

fileprivate var isUrl : Bool//是否通过url加载图片

fileprivate let isHorizontalScroll : Bool//是否为横向滚动
fileprivate var imgArray : Array<UIImage>//显示的图片

fileprivate let scrollView = UIScrollView()//
fileprivate let pageControl = UIPageControl()//
fileprivate var timer = Timer()//

fileprivate var imgIndex : Int//当前显示的图片的索引
fileprivate var isAutoScrolling : Bool//是否为自动滚动状态

fileprivate let imgV1 = UIImageView()//
fileprivate let imgV2 = UIImageView()//
fileprivate let imgV3 = UIImageView()//



init(frame: CGRect, imgArray: Array<UIImage>, isHorizontalScroll: Bool, delegate: LYBannerViewDelegate) {
self.imgArray = imgArray
self.isHorizontalScroll = isHorizontalScroll
self.delegate = delegate

self.currentColor = UIColor.red
self.normalColor = UIColor.white
self.showPageControl = true
self.imgIndex = 0
self.isAutoScrolling = true
self.customerTitleArray = Array()
self.customerImgArray = Array()
self.imgUrlArray = Array()
self.isUrl = false

super.init(frame:frame)
self.frame = frame

self.setUpSubviews()

}

required init?(coder aDecoder: NSCoder) {
fatalError("init(coder:) has not been implemented")
}


init(frame: CGRect, titleArray: Array<String>, isHorizontalScroll: Bool, delegate: LYBannerViewDelegate) {
self.imgArray = Array()
self.isHorizontalScroll = isHorizontalScroll
self.delegate = delegate

self.currentColor = UIColor.red
self.normalColor = UIColor.white
self.showPageControl = true
self.imgIndex = 0
self.isAutoScrolling = true
self.customerTitleArray = Array()
self.customerImgArray = Array()
self.imgUrlArray = Array()
self.isUrl = false

super.init(frame:frame)
self.frame = frame
self.imgArray = self.convertStringArrayToImageArray(stringArray: titleArray)

self.setUpSubviews()
}


init(frame: CGRect, isHorizontalScroll: Bool, delegate: LYBannerViewDelegate) {

self.isHorizontalScroll = isHorizontalScroll
self.delegate = delegate

self.currentColor = UIColor.red
self.normalColor = UIColor.white
self.showPageControl = true
self.imgIndex = 0
self.isAutoScrolling = true
self.imgArray = Array()
self.customerTitleArray = Array()
self.customerImgArray = Array()
self.imgUrlArray = Array()
self.isUrl = false

super.init(frame:frame)
self.frame = frame

self.setUpSubviews()
}


}

extension LYBannerView{
func setUpSubviews() {
self.imgIndex = 0

if self.isUrl{
//1.图片至少为2张
if self.imgUrlArray.count == 0{
let imgUrl = "http://www.7xiaofu.com/UPLOAD/sys/2017-03-07/~UPLOAD~sys~2017-03-07@1488850751.jpg"
self.imgUrlArray.insert(imgUrl, at: 0)
self.imgUrlArray.insert(imgUrl, at: 1)
self.scrollView.isScrollEnabled = false
}else if self.imgUrlArray.count == 1{
self.imgUrlArray.insert(self.imgUrlArray[0], at: 1)
self.scrollView.isScrollEnabled = false
}else{
self.scrollView.isScrollEnabled = true

//4.定时器
self.setUpTimer()
}

}else{
//1.图片至少为2张
if self.imgArray.count == 0{
let img = UIImage()
self.imgArray.insert(img, at: 0)
self.imgArray.insert(img, at: 1)
self.scrollView.isScrollEnabled = false
}else if self.imgArray.count == 1{
self.imgArray.insert(self.imgArray[0], at: 1)
self.scrollView.isScrollEnabled = false
}else{
self.scrollView.isScrollEnabled = true

//4.定时器
self.setUpTimer()
}

}

//2.设置scroll
self.setUpScrollView()

//3.pagecontrol
self.setUpPageControl()

}

/**
通过三个imageview，每次滚动或者手动滑动后都重新设置imageview的图片，并且保证scrollview显示的是中间的imageview
*/
func setUpScrollView() {
self.scrollView.frame = self.bounds
self.scrollView.backgroundColor = UIColor.clear
if self.isHorizontalScroll{
self.scrollView.contentSize = CGSize(width: self.frame.width * 3, height: self.frame.height)
}else{
self.scrollView.contentSize = CGSize(width: self.frame.width, height: self.frame.height * 3)
}
self.scrollView.delegate = self
self.scrollView.isPagingEnabled = true
self.scrollView.showsVerticalScrollIndicator = false
self.scrollView.showsHorizontalScrollIndicator = false
self.scrollView.bounces = false
self.addSubview(self.scrollView)

var orginX : CGFloat
var orginY : CGFloat
if self.isHorizontalScroll{
orginX = self.frame.width
orginY = 0
}else{
orginX = 0
orginY = self.frame.height
}
self.imgV1.frame = CGRect(x:0, y:0, width:self.frame.width, height:self.frame.height)
self.imgV1.backgroundColor = UIColor.clear
self.imgV1.contentMode = .scaleAspectFit
self.imgV1.addTapAction(action: #selector(LYBannerView.imageViewClickAction), target: self)
self.imgV2.frame = CGRect(x:orginX, y:orginY, width:self.frame.width, height:self.frame.height)
self.imgV2.backgroundColor = UIColor.clear
self.imgV2.contentMode = .scaleAspectFit
self.imgV2.addTapAction(action: #selector(LYBannerView.imageViewClickAction), target: self)
self.imgV3.frame = CGRect(x:orginX * 2, y:orginY * 2, width:self.frame.width, height:self.frame.height)
self.imgV3.backgroundColor = UIColor.clear
self.imgV3.contentMode = .scaleAspectFit
self.imgV3.addTapAction(action: #selector(LYBannerView.imageViewClickAction), target: self)

self.scrollView.addSubview(self.imgV1)
self.scrollView.addSubview(self.imgV2)
self.scrollView.addSubview(self.imgV3)

self.reSetUpImageViewOfScrollView()
}

/**重新排布ScrollView中的ImageView*/
func reSetUpImageViewOfScrollView() {
if self.isUrl{
if self.imgIndex >= self.imgUrlArray.count{
self.imgIndex = 0
}else if self.imgIndex < 0{
self.imgIndex = self.imgUrlArray.count - 1
}

self.pageControl.currentPage = self.imgIndex

self.imgV2.kf.setImage(with: URL(string:self.imgUrlArray[self.imgIndex]),placeholder:#imageLiteral(resourceName: "banner1"))
if self.imgIndex == 0{
self.imgV1.kf.setImage(with: URL(string:self.imgUrlArray[self.imgUrlArray.count - 1]),placeholder:#imageLiteral(resourceName: "banner1"))
self.imgV3.kf.setImage(with: URL(string:self.imgUrlArray[self.imgIndex + 1]),placeholder:#imageLiteral(resourceName: "banner1"))
}else if self.imgIndex == self.imgUrlArray.count - 1{
self.imgV1.kf.setImage(with: URL(string:self.imgUrlArray[self.imgIndex - 1]),placeholder:#imageLiteral(resourceName: "banner1"))
self.imgV3.kf.setImage(with: URL(string:self.imgUrlArray[0]))
}else{
self.imgV1.kf.setImage(with: URL(string:self.imgUrlArray[self.imgIndex - 1]),placeholder:#imageLiteral(resourceName: "banner1"))
self.imgV3.kf.setImage(with: URL(string:self.imgUrlArray[self.imgIndex + 1]),placeholder:#imageLiteral(resourceName: "banner1"))
}


if self.isHorizontalScroll{
self.scrollView.setContentOffset(CGPoint(x:self.frame.width, y:0), animated: false)
}else{
self.scrollView.setContentOffset(CGPoint(x:0, y:self.frame.height), animated: false)
}

}else{
if self.imgIndex >= self.imgArray.count{
self.imgIndex = 0
}else if self.imgIndex < 0{
self.imgIndex = self.imgArray.count - 1
}

self.pageControl.currentPage = self.imgIndex

self.imgV2.image = self.imgArray[self.imgIndex]
if self.imgIndex == 0{
self.imgV1.image = self.imgArray[self.imgArray.count - 1];
self.imgV3.image = self.imgArray[self.imgIndex + 1]
}else if self.imgIndex == self.imgArray.count - 1{
self.imgV1.image = self.imgArray[self.imgIndex - 1];
self.imgV3.image = self.imgArray[0]
}else{
self.imgV1.image = self.imgArray[self.imgIndex - 1];
self.imgV3.image = self.imgArray[self.imgIndex + 1]
}


if self.isHorizontalScroll{
self.scrollView.setContentOffset(CGPoint(x:self.frame.width, y:0), animated: false)
}else{
self.scrollView.setContentOffset(CGPoint(x:0, y:self.frame.height), animated: false)
}

}

}


/**pagecontrol*/
func setUpPageControl() {

if !self.showPageControl{
return
}

self.pageControl.frame = CGRect(x:0, y:self.frame.height - 20, width:self.frame.width, height:20)
self.pageControl.backgroundColor = UIColor.clear
self.pageControl.numberOfPages = self.isUrl ? self.imgUrlArray.count : self.imgArray.count
self.pageControl.currentPageIndicatorTintColor = self.currentColor
self.pageControl.pageIndicatorTintColor = self.normalColor
self.pageControl.currentPage = 0
self.pageControl.hidesForSinglePage = true
self.addSubview(self.pageControl)
}

//设置定时器
func setUpTimer()  {
if self.timer.isValid{
self.timer.invalidate()
}
self.timer = Timer(timeInterval: 2.0, target: self, selector: #selector(LYBannerView.changeImage), userInfo: nil, repeats: true)
RunLoop.main.add(self.timer, forMode: .defaultRunLoopMode)
timer.fire()
self.isAutoScrolling = true
}

@objc func changeImage(){
if isAutoScrolling {
self.imgIndex += 1
if self.isHorizontalScroll {
self.scrollView.setContentOffset(CGPoint(x:self.frame.width * 2, y:0), animated: true)
}else{
self.scrollView.setContentOffset(CGPoint(x:0, y:self.frame.height * 2), animated: true)
}
self.reSetUpImageViewOfScrollView()
}
}

}



extension LYBannerView : UIScrollViewDelegate{
func scrollViewDidScroll(_ scrollView: UIScrollView) {

}

func scrollViewWillBeginDragging(_ scrollView: UIScrollView) {
self.timer.invalidate()
self.isAutoScrolling = false
}

func scrollViewDidEndDragging(_ scrollView: UIScrollView, willDecelerate decelerate: Bool) {

}

func scrollViewDidEndScrollingAnimation(_ scrollView: UIScrollView) {
}

func scrollViewDidEndDecelerating(_ scrollView: UIScrollView) {

var showIndex : CGFloat

if self.isHorizontalScroll{
showIndex = scrollView.contentOffset.x / self.frame.width
}else{
showIndex = scrollView.contentOffset.y / self.frame.height
}

if showIndex == 0{
//当前显示的第一个imgv
self.imgIndex -= 1
self.reSetUpImageViewOfScrollView()
}else if showIndex == 1{
//当前显示的第二个imgv

}else if showIndex == 2{
//当前显示的第三个imgv
self.imgIndex += 1
self.reSetUpImageViewOfScrollView()
}

self.setUpTimer()
}
}

extension LYBannerView{
//图片点击事件处理
func imageViewClickAction() {
self.delegate?.lyBannerClick(lyBanner:self, index: self.imgIndex)
}
}


//显示滚动文字
extension LYBannerView{
func convertStringArrayToImageArray(stringArray:Array<String>) -> Array<UIImage> {
let arrM = NSMutableArray()
for s in stringArray{
let lbl = UILabel(frame:self.bounds)
lbl.text = s
lbl.font = UIFont.systemFont(ofSize: 14.0)
lbl.textAlignment = .center
let image = self.converViewToImage(v: lbl)
arrM.add(image)
}
return arrM as! Array<UIImage>
}

//label转image
func converViewToImage(v:UIView) -> UIImage {
let s = v.bounds.size
// 下面方法，第一个参数表示区域大小。第二个参数表示是否是非透明的。如果需要显示半透明效果，需要传false，否则传true。第三个参数就是屏幕密度了
UIGraphicsBeginImageContextWithOptions(s, false, UIScreen.main.scale)
v.layer.render(in: UIGraphicsGetCurrentContext()!)
let image = UIGraphicsGetImageFromCurrentImageContext()
UIGraphicsEndImageContext()
return image!
}

}




```
