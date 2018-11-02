iOS 屏幕方向设备方向的理解

//开始监听屏幕旋转
UIDevice.current.beginGeneratingDeviceOrientationNotifications()

// 监测设备方向
NotificationCenter.default.addObserver(self, selector: #selector(LYPlayerView.onDeviceOrientationChange), name: NSNotification.Name.UIDeviceOrientationDidChange, object: nil)

//状态条变化
NotificationCenter.default.addObserver(self, selector: #selector(LYPlayerView.onStatusBarOrientationChange), name: NSNotification.Name.UIApplicationDidChangeStatusBarOrientation, object: nil)

// 监测设备方向
@objc private func onDeviceOrientationChange() {
self.setPortraitAndLandscapeFrame()
}

//状态条方向变化(屏幕方向变化)
@objc private func onStatusBarOrientationChange() {
self.setPortraitAndLandscapeFrame()
}


UIInterfaceOrientation
// Note that UIInterfaceOrientationLandscapeLeft is equal to UIDeviceOrientationLandscapeRight (and vice versa).
// This is because rotating the device to the left requires rotating the content to the right.
public enum UIInterfaceOrientation : Int {

case unknown

case portrait

case portraitUpsideDown

case landscapeLeft  //状态栏朝右，按钮在左

case landscapeRight
}


UIInterfaceOrientationMask
public struct UIInterfaceOrientationMask : OptionSet {

public init(rawValue: UInt)


public static var portrait: UIInterfaceOrientationMask { get }

public static var landscapeLeft: UIInterfaceOrientationMask { get }

public static var landscapeRight: UIInterfaceOrientationMask { get }

public static var portraitUpsideDown: UIInterfaceOrientationMask { get }

public static var landscape: UIInterfaceOrientationMask { get }

public static var all: UIInterfaceOrientationMask { get }

public static var allButUpsideDown: UIInterfaceOrientationMask { get }
}



UIDeviceOrientation
public enum UIDeviceOrientation : Int {


case unknown

case portrait // Device oriented vertically, home button on the bottom

case portraitUpsideDown // Device oriented vertically, home button on the top

case landscapeLeft // Device oriented horizontally, home button on the right

case landscapeRight // Device oriented horizontally, home button on the left //状态栏朝右，home按钮在左

case faceUp // Device oriented flat, face up

case faceDown // Device oriented flat, face down
}
