## iOS 事件以及手势的处理

##首先引用[深入浅出iOS事件机制](http://zhoon.github.io/ios/2015/04/12/ios-event.html)，[iOS触摸事件处理详解](http://www.jianshu.com/p/cb0314b72883)，[详解iOS触摸事件与手势识别](http://www.jianshu.com/p/77139b374313)三篇博客里的一些概念

UIResponser就是用来接收和处理事件的类，先抛开iOS中的具体传递细节，系统发送UIEvent的Touch message给UIResponser类。UIResponser提供了一下几个函数来做事件处理
UIResponser包括了各种Touch message 的处理，比如开始，移动，停止等等。常见的UIResponser有 UIView及子类，UIViController,APPDelegate，UIApplication等等。
```base
//触摸事件
- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(nullable UIEvent *)event;
- (void)touchesMoved:(NSSet<UITouch *> *)touches withEvent:(nullable UIEvent *)event;
- (void)touchesEnded:(NSSet<UITouch *> *)touches withEvent:(nullable UIEvent *)event;
- (void)touchesCancelled:(NSSet<UITouch *> *)touches withEvent:(nullable UIEvent *)event;
- (void)touchesEstimatedPropertiesUpdated:(NSSet<UITouch *> *)touches NS_AVAILABLE_IOS(9_1);

//物理按钮，遥控器上面的按钮在按压状态等状态下的回调
- (void)pressesBegan:(NSSet<UIPress *> *)presses withEvent:(nullable UIPressesEvent *)event NS_AVAILABLE_IOS(9_0);
- (void)pressesChanged:(NSSet<UIPress *> *)presses withEvent:(nullable UIPressesEvent *)event NS_AVAILABLE_IOS(9_0);
- (void)pressesEnded:(NSSet<UIPress *> *)presses withEvent:(nullable UIPressesEvent *)event NS_AVAILABLE_IOS(9_0);
- (void)pressesCancelled:(NSSet<UIPress *> *)presses withEvent:(nullable UIPressesEvent *)event NS_AVAILABLE_IOS(9_0);

//设备的陀螺仪和加速传感器使用
- (void)motionBegan:(UIEventSubtype)motion withEvent:(nullable UIEvent *)event NS_AVAILABLE_IOS(3_0);
- (void)motionEnded:(UIEventSubtype)motion withEvent:(nullable UIEvent *)event NS_AVAILABLE_IOS(3_0);
- (void)motionCancelled:(UIEventSubtype)motion withEvent:(nullable UIEvent *)event NS_AVAILABLE_IOS(3_0);

```
#响应链：
1.程序启动时，UIApplication会生成一个单例，并会关联一个APPDelegate。APPDelegate作为整个响应链的根建立起来，UIApplication的nextResponser为APPDelegate。
2.程序启动后，任何的UIWindow被创建时，UIWindow内部都会把nextResponser设置为UIApplication单例。
3.UIWindow初始化rootViewController, rootViewController的nextResponser会设置为UIWindow。
4.UIViewController初始化View，View的nextResponser会设置为rootViewController。
5.AddSubView时，如果subView不是ViewController的View,那么subView的nextResponser会被设置为superView。否则就是 subView -> subView.VC ->superView。

#查找响应者
```base
//寻找响应的view
- (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event;
//判断点是否在视图内
- (BOOL)pointInside:(CGPoint)point withEvent:(UIEvent *)event;
```
当向UIWindow发送hitTest:withEvent:消息时，hitTest:withEvent:里面所做的事，就是判断当前的点击位置是否在window里面，如果在则遍历window的subview然后依次对subview发送hitTest:withEvent:消息(注意这里给subview发送消息是根据当前subview的index顺序，index越大就越先被访问)。如果当前的point没有在view上面，那么这个view的subview也就不会被遍历了。当遍历到某view且此view没有subview或者是点的位置不在subview中那么这个view就是所找的响应者。
在寻找过程中会判断当前view是否可响应事件，比如userInteractionEnabled、hidden、alpha等属性，都会影响一个view是否可以响应事件，如果不响应则直接返回nil

我们平时加到UIScrollView(或者UITableView和UICollection)上面的UIButton，即使有设置highLighted的样式，点击的时候却发现这个样式老是不出来，但是按钮的事件明明可以响应的，很诡异。后来才知道，UIScrollView因为要滚动，所以对事件做了特殊的处理： 当UIScrollView接收到事件之后，会暂时劫持当前的事件300毫秒，如果300毫秒之后手指还没有滚动，则认为你放弃滚动，放弃对事件的劫持并往下传递，但是从Time Profiler看到此时按钮并不是调用自身的touch方法，而是调用自身绑定的手势的touch事件，由于按钮的highLighted样式是写在按钮的touch方法上的，所以这个这个时候就看不到高亮了。但是长按按钮缺可以让按钮有高亮的状态，这个就不太清楚为什么了，因为从Time Profiler里面看按钮的touchesBegan好像还是没有被调。 如果300毫秒之内手指滚动了，则响应滚动的事件，事件就不会继续传给subView了，也就是不会继续调用按钮上手势的touch方法了。可以通过UIScrollView的一个属性来解决这个问题：delaysContentTouches，意思是是否需要延迟处理事件的传递，默认是NO。把delaysContentTouches设置为YES之后，一切看起来挺好的，按钮终于有高亮样式了哈哈哈，但是发现另一个问题：如果手指点击在按钮上面并滚动UIScrollView，发现怎么也滚动不了。原因是当手指点击UIScrollView并在滚动之前，如果subView接收并且可以响应事件(delaysContentTouches设置为YES)，则事件响应链会在subView响应事件之后就截断，即UIScrollView本身不会响应到此事件，不会发生滚动。可以设置canCancelContentTouches为YES来让UIScrollView可以滚动，与之类似的还有一个touchesShouldCancelInContentView:接口，可以根据参数view来更方便的判断是否需要cancel，如果有需要可以在UIScrollView的子类里面重写这个接口。
