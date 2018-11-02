iOS 屏幕方向设备方向的理解

//开始监听屏幕旋转，如果不设置开始，则无法
UIDevice.current.beginGeneratingDeviceOrientationNotifications()
//结束监听屏幕旋转，离开页面的时间要停止监听设备方向的变化
UIDevice.current.endGeneratingDeviceOrientationNotifications()

// 监测设备方向变化
NotificationCenter.default.addObserver(self, selector: #selector(LYPlayerView.onDeviceOrientationChange), name: NSNotification.Name.UIDeviceOrientationDidChange, object: nil)
// 监测设备方向
@objc private func onDeviceOrientationChange() {
let deviceOrientation = UIDevice.current.orientation
}

//监听屏幕内容方向变化
NotificationCenter.default.addObserver(self, selector: #selector(LYPlayerView.onStatusBarOrientationChange), name: NSNotification.Name.UIApplicationDidChangeStatusBarOrientation, object: nil)
//状态条方向变化(屏幕方向变化)
@objc private func onStatusBarOrientationChange() {
let currentOrientation = UIApplication.shared.statusBarOrientation
}

当同时监听设备方向和屏幕方向的变化时，会首先收到屏幕方向变化的通知，然后收到设备方向变化的通知，如果在屏幕方向变化的通知里面做页面的调整会出现x与y还是原来值的问题，因此最好在设备方向变化的通知里面做页面布局的操作。

//当前支持的屏幕方向
let supportOrientationMask = UIApplication.shared.supportedInterfaceOrientations(for: UIApplication.shared.keyWindow)

//app支持方向
UIInterfaceOrientationMask
public struct UIInterfaceOrientationMask : OptionSet {
public init(rawValue: UInt)
public static var portrait: UIInterfaceOrientationMask { get }  //垂直方向，home键在下
public static var landscapeLeft: UIInterfaceOrientationMask { get }  //横屏，home键在左
public static var landscapeRight: UIInterfaceOrientationMask { get }  //横屏，home键在右
public static var portraitUpsideDown: UIInterfaceOrientationMask { get }  //垂直方向，home键在上
public static var landscape: UIInterfaceOrientationMask { get }  //横屏
public static var all: UIInterfaceOrientationMask { get }  //所有方向
public static var allButUpsideDown: UIInterfaceOrientationMask { get }  //除home键在上外的所有方向
}

//屏幕方向
UIInterfaceOrientation
// Note that UIInterfaceOrientationLandscapeLeft is equal to UIDeviceOrientationLandscapeRight (and vice versa).
// This is because rotating the device to the left requires rotating the content to the right.
//将设备横屏转向左边的时候，屏幕的方向需要向右转
public enum UIInterfaceOrientation : Int {
case unknown  //未知方向
case portrait  //垂直方向，home键在下
case portraitUpsideDown  //垂直方向，home键在上
case landscapeLeft  //状态栏朝右，home键在左
case landscapeRight  //状态栏朝左，home键在右

//设备方向
UIDeviceOrientation
public enum UIDeviceOrientation : Int {
case unknown  //未知方向
case portrait // Device oriented vertically, home button on the bottom  //垂直方向，home键在下
case portraitUpsideDown // Device oriented vertically, home button on the top  //垂直方向，home键在上
case landscapeLeft // Device oriented horizontally, home button on the right  //状态栏朝左，home按钮在右
case landscapeRight // Device oriented horizontally, home button on the left //状态栏朝右，home按钮在左
case faceUp // Device oriented flat, face up  //平放设备时屏幕向上
case faceDown // Device oriented flat, face down  //平放设备时屏幕向下
}
