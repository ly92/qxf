

## 支持 年 月 日 时 分 的时间选择器

在公司的项目中要求选择时间的时候能够兼顾到年月日时分于是便整理了一个时间选择的工具类，最近正在学习Swift，后面抽空将会写出一个Swift版本的，如果我还未来得及写恰巧您需要使用可以联系我：1364757394@qq.com，免费技术分享

## 1、文件介绍
```base
NSCalendar+LY.h    NSCalendar+LY.m
STPickerDate.h     STPickerDate.m
STPickerView.h     STPickerView.m
```
其中NSCalendar+LY为NSCalendar的分类，主要用来计算当前时间，STPickerDate中主要实现对UIPickerView的自定义显示，STPickerView是选择器显示的页面布局
## 2、使用示例


## 3、源码

NSCalendar+LY.h 
```base
#import <Foundation/Foundation.h>

@interface NSCalendar (ST)

/**
*  1.当前的日期数据元件模型
*
*  @return <#return value description#>
*/
+ (NSDateComponents *)currentDateComponents;

/**
*  2.当前年
*
*  @return <#return value description#>
*/
+ (NSInteger)currentYear;

/**
*  3.当前月
*
*  @return <#return value description#>
*/
+ (NSInteger)currentMonth;

/**
*  4.当前天
*/
+ (NSInteger)currentDay;
/**
*  4.当前小时
*/
+ (NSInteger)currentHour;
/**
*  4.当前分钟
*/
+ (NSInteger)currentMinute;
/**
*  5.当前周数
*/
+ (NSInteger)currnentWeekday;

/**
*  6.获取指定年月的天数
*/
+ (NSInteger)getDaysWithYear:(NSInteger)year
month:(NSInteger)month;

/**
*  7.获取指定年月的第一天的周数
*/
+ (NSInteger)getFirstWeekdayWithYear:(NSInteger)year
month:(NSInteger)month;
/**
*  8.比较两个日期元件
*/
+ (NSComparisonResult)compareWithComponentsOne:(NSDateComponents *)componentsOne
componentsTwo:(NSDateComponents *)componentsTwo;

/**
*  9.获取两个日期元件之间的日期元件
*/
+ (NSMutableArray *)arrayComponentsWithComponentsOne:(NSDateComponents *)componentsOne
componentsTwo:(NSDateComponents *)componentsTwo;
/**
*  10.字符串转日期元件 字符串格式为：yy-MM-dd
*/
+ (NSDateComponents *)dateComponentsWithString:(NSString *)String;
@end

```
NSCalendar+LY.m
```base
#import "NSCalendar+ST.h"

@implementation NSCalendar (ST)



+ (NSDateComponents *)currentDateComponents
{
NSCalendar *calendar = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
NSInteger unitFlags = NSCalendarUnitYear | NSCalendarUnitMonth | NSCalendarUnitDay | NSCalendarUnitHour| NSCalendarUnitMinute| NSCalendarUnitWeekday;
return [calendar components:unitFlags fromDate:[NSDate date]];
}

+ (NSInteger)currentMonth
{
return [NSCalendar currentDateComponents].month;
}

+ (NSInteger)currentYear
{
return [NSCalendar currentDateComponents].year;
}

+ (NSInteger)currentDay
{
return [NSCalendar currentDateComponents].day;
}

+ (NSInteger)currentHour
{
return [NSCalendar currentDateComponents].hour;
}
+ (NSInteger)currentMinute
{
return [NSCalendar currentDateComponents].minute;
}



+ (NSInteger)currnentWeekday
{
return [NSCalendar currentDateComponents].weekday;
}

+ (NSInteger)getDaysWithYear:(NSInteger)year
month:(NSInteger)month
{

//    NSLog(@"year:%ld---month:%ld",(long)year,(long)month);

switch (month) {
case 1:
return 31;
break;
case 2:
if (year%400==0 || (year%100!=0 && year%4 == 0)) {
return 29;
}else{
return 28;
}
break;
case 3:
return 31;
break;
case 4:
return 30;
break;
case 5:
return 31;
break;
case 6:
return 30;
break;
case 7:
return 31;
break;
case 8:
return 31;
break;
case 9:
return 30;
break;
case 10:
return 31;
break;
case 11:
return 30;
break;
case 12:
return 31;
break;
default:
return 0;
break;
}
}

+ (NSInteger)getFirstWeekdayWithYear:(NSInteger)year
month:(NSInteger)month
{
NSString *stringDate = [NSString stringWithFormat:@"%ld-%ld-01", (long)year, (long)month];
NSDateFormatter *formatter = [[NSDateFormatter alloc]init];
[formatter setDateFormat:@"yy-MM-dd"];
NSDate *date = [formatter dateFromString:stringDate];

NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
NSDateComponents *components = [gregorian components:(NSCalendarUnitDay | NSCalendarUnitMonth | NSCalendarUnitYear | NSCalendarUnitWeekday) fromDate:date];
return [components weekday];
}

+ (NSComparisonResult)compareWithComponentsOne:(NSDateComponents *)componentsOne
componentsTwo:(NSDateComponents *)componentsTwo
{
if (componentsOne.year == componentsTwo.year &&
componentsOne.month == componentsTwo.month &&
componentsOne.day   == componentsTwo.day) {
return NSOrderedSame;
}else if (componentsOne.year < componentsTwo.year ||
(componentsOne.year == componentsTwo.year && componentsOne.month < componentsTwo.month) ||
(componentsOne.year == componentsTwo.year && componentsOne.month == componentsTwo.month && componentsOne.day < componentsTwo.day)) {
return NSOrderedAscending;
}else {
return NSOrderedDescending;
}
}

+ (NSMutableArray *)arrayComponentsWithComponentsOne:(NSDateComponents *)componentsOne
componentsTwo:(NSDateComponents *)componentsTwo
{
NSMutableArray *arrayComponents = [NSMutableArray array];

NSString *stringOne = [NSString stringWithFormat:@"%ld-%ld-%ld", componentsOne.year,
componentsOne.month,
componentsOne.day];
NSString *stringTwo = [NSString stringWithFormat:@"%ld-%ld-%ld", componentsTwo.year,
componentsTwo.month,
componentsTwo.day];
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc]init];
[dateFormatter setDateFormat:@"yy-MM-dd"];

NSDate *dateFromString = [dateFormatter dateFromString:stringOne];
NSDate *dateToString = [dateFormatter dateFromString:stringTwo];
int timediff = [dateToString timeIntervalSince1970]-[dateFromString timeIntervalSince1970];

NSTimeInterval timeInterval = [dateFromString timeIntervalSinceDate:dateFromString];

for (int i = 0; i <= timediff; i+=86400) {
timeInterval = i;
NSDate *date = [dateFromString dateByAddingTimeInterval:timeInterval];

NSCalendar *calendar = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
NSInteger unitFlags = NSCalendarUnitYear | NSCalendarUnitMonth | NSCalendarUnitDay | NSCalendarUnitWeekday;
[arrayComponents addObject:[calendar components:unitFlags fromDate:date]];
}
return arrayComponents;
}

+ (NSDateComponents *)dateComponentsWithString:(NSString *)String
{
NSDateFormatter *formatter = [[NSDateFormatter alloc]init];
[formatter setDateFormat:@"yy-MM-dd"];
NSDate *date = [formatter dateFromString:String];

NSCalendar *calendar = [NSCalendar currentCalendar];
NSInteger unitFlags = NSCalendarUnitYear | NSCalendarUnitMonth | NSCalendarUnitDay | NSCalendarUnitWeekday;
return  [calendar components:unitFlags fromDate:date];
}
@end

```

STPickerDate.h
```base
#import "STPickerView.h"
NS_ASSUME_NONNULL_BEGIN
@class STPickerDate;
@protocol  STPickerDateDelegate<NSObject>
- (void)pickerDate:(STPickerDate *)pickerDate year:(NSInteger)year month:(NSInteger)month day:(NSInteger)day hour:(NSInteger)hour minute:(NSInteger)minute;

@end
@interface STPickerDate : STPickerView

/** 1.最小的年份，default is 1900 */
@property (nonatomic, assign)NSInteger yearLeast;
/** 2.显示年份数量，default is 200 */
@property (nonatomic, assign)NSInteger yearSum;
/** 3.中间选择框的高度，default is 28*/
@property (nonatomic, assign)CGFloat heightPickerComponent;

@property(nonatomic, weak)id <STPickerDateDelegate>delegate ;




@property(nonatomic, copy) void (^pickerDate5Block)(NSInteger year,NSInteger month,NSInteger day,NSInteger hour,NSInteger minute,NSString * time);
@property(nonatomic, copy) void (^pickerDate4Block)(NSInteger year,NSInteger month,NSInteger day,NSInteger hour,NSString * time);
@property(nonatomic, copy) void (^pickerDate3Block)(NSInteger year,NSInteger month,NSInteger day,NSString * time);
@property(nonatomic, copy) void (^pickerDate3EndBlock)(NSInteger year,NSInteger month,NSInteger day,NSString * time);
@property(nonatomic, copy) void (^pickerDateAndRowBlock)(NSInteger year,NSInteger month,NSInteger day,NSInteger row,NSString * time);
@property(nonatomic, copy) void (^pickerDate1Block)(NSInteger year);



@end
NS_ASSUME_NONNULL_END

```

STPickerDate.m
```base
#import "STPickerDate.h"
#import "NSCalendar+ST.h"
#define screenWith  [UIScreen mainScreen].bounds.size.width
#define screenHeight [UIScreen mainScreen].bounds.size.height
@interface STPickerDate()<UIPickerViewDataSource, UIPickerViewDelegate>
/** 1.年 */
@property (nonatomic, assign)NSInteger year;
/** 2.月 */
@property (nonatomic, assign)NSInteger month;
/** 3.日 */
@property (nonatomic, assign)NSInteger day;
/** 4.时 */
@property (nonatomic, assign)NSInteger hour;
/** 5.分 */
@property (nonatomic, assign)NSInteger minute;
/** 6.秒 */
//@property (nonatomic, assign)NSInteger minute;


@end

@implementation STPickerDate

#pragma mark - --- init 视图初始化 ---

- (void)setupUI {



self.title = @"请选择日期";

_yearLeast = 1900;
_yearSum   = 200;
_heightPickerComponent = 28;

_year  = [NSCalendar currentYear];
_month = [NSCalendar currentMonth];
_day   = [NSCalendar currentDay];
_hour   = [NSCalendar currentHour];
_minute   = [NSCalendar currentMinute];

[self.pickerView setDelegate:self];
[self.pickerView setDataSource:self];

[self.pickerView selectRow:(_year - _yearLeast) inComponent:0 animated:NO];

if(self.rows > 1){
[self.pickerView selectRow:(_month - 1) inComponent:1 animated:NO];
}
if(self.rows > 2){
[self.pickerView selectRow:(_day - 1) inComponent:2 animated:NO];
}
if (self.rows > 3) {
[self.pickerView selectRow:(_hour) inComponent:3 animated:NO];
}
if (self.rows > 4) {
[self.pickerView selectRow:(_minute) inComponent:4 animated:NO];
}

}

#pragma mark - --- delegate 视图委托 ---

- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView
{
return self.rows;
}

- (NSInteger)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component{

switch (component) {
case 0:
{
return self.yearSum;
}
break;
case 1:
{
return 12;
}
break;
case 2:
{
//            NSInteger yearSelected = [pickerView selectedRowInComponent:0] + self.yearLeast;
//            NSInteger monthSelected = [pickerView selectedRowInComponent:1] + 1;

NSInteger dayNum = [NSCalendar getDaysWithYear:self.year month:self.month];

//            NSLog(@"------%ld",(long)dayNum);

return  dayNum;
}
break;
case 3:
{
return 24;
}
break;
case 4:
{
return 60;
}
break;
default:
break;
}
return 0;
}

- (CGFloat)pickerView:(UIPickerView *)pickerView rowHeightForComponent:(NSInteger)component{
return self.heightPickerComponent;
}

- (UIView *)pickerView:(UIPickerView *)pickerView viewForRow:(NSInteger)row forComponent:(NSInteger)component reusingView:(nullable UIView *)view
{

UILabel*label=[[UILabel alloc]initWithFrame:CGRectMake(screenWith*component/6.0, 0,screenWith/6.0, 30)];
label.font=[UIFont systemFontOfSize:15.0];
label.tag=component*100+row;
label.textAlignment=NSTextAlignmentCenter;
switch (component) {
case 0:
{
label.frame=CGRectMake(5, 0,screenWith/4.0, 30);
label.text=[NSString stringWithFormat:@"%ld年",(long)(_yearLeast + row)];
}
break;
case 1:
{
label.frame=CGRectMake(screenWith/4.0, 0, screenWith/8.0, 30);
label.text=[NSString stringWithFormat:@"%ld月",(long)row+1];
}
break;
case 2:
{
label.frame=CGRectMake(screenWith*3/8, 0, screenWith/8.0, 30);
label.text=[NSString stringWithFormat:@"%ld日",(long)row+1];
}
break;
case 3:
{
label.textAlignment=NSTextAlignmentRight;
label.text=[NSString stringWithFormat:@"%ld时",(long)row];
}
break;
case 4:
{
label.textAlignment=NSTextAlignmentRight;
label.text=[NSString stringWithFormat:@"%ld分",(long)row];
}
break;
case 5:
{
label.textAlignment=NSTextAlignmentRight;
label.frame=CGRectMake(screenWith*component/6.0, 0, screenWith/6.0-5, 30);
label.text=[NSString stringWithFormat:@"%ld秒",(long)row];
}
break;

default:
break;
}
return label;

}
- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component
{
[self reloadData];

switch (component) {
case 0:
if (self.rows > 1){
[pickerView reloadComponent:1];
}
if (self.rows >2){
[pickerView reloadComponent:2];
}
break;
case 1:
if (self.rows > 2){
[pickerView reloadComponent:2];
}
default:
break;
}
}


#pragma mark - --- event response 事件相应 ---

- (void)selectedOk
{
if ([self.delegate respondsToSelector:@selector(pickerDate:year:month:day:hour:minute:)]) {
[self.delegate pickerDate:self year:self.year month:self.month day:self.day hour:self.hour minute:self.minute];
}

NSString * selectTime =[NSString stringWithFormat:@"%ld.%.2ld.%.2ld %.2ld:%.2ld",self.year,self.month,self.day,self.hour ,self.minute];

if (_pickerDate5Block) {
_pickerDate5Block(self.year,self.month,self.day,self.hour,self.minute,selectTime);
}
if (_pickerDate4Block) {
_pickerDate4Block(self.year,self.month,self.day,self.hour,selectTime);
}
if (_pickerDate3Block) {

selectTime =[NSString stringWithFormat:@"%ld.%.2ld.%.2ld %.2ld:%.2ld",self.year,self.month,self.day,self.hour,self.minute];
_pickerDate3Block(self.year,self.month,self.day,selectTime);
}
if (_pickerDate3EndBlock) {

selectTime =[NSString stringWithFormat:@"%ld.%.2ld.%.2ld %.2d:%.2d",self.year,self.month,self.day,23,00];
_pickerDate3EndBlock(self.year,self.month,self.day,selectTime);
}
if (_pickerDateAndRowBlock){
selectTime =[NSString stringWithFormat:@"%ld.%.2ld.%.2ld %.2ld:%.2ld",self.year,self.month,self.day,self.hour,self.minute];
_pickerDateAndRowBlock(self.year,self.month,self.day,self.rows,selectTime);
}




if (_pickerDate1Block) {
_pickerDate1Block(self.year);
}
DeLog(@"-----  %@",selectTime);
[super selectedOk];
}

#pragma mark - --- private methods 私有方法 ---

- (void)reloadData
{
self.year  = [self.pickerView selectedRowInComponent:0] + self.yearLeast;

if (self.rows > 1) {
self.month = [self.pickerView selectedRowInComponent:1] + 1;
}
if (self.rows > 2) {
self.day   = [self.pickerView selectedRowInComponent:2] + 1;
}
if (self.rows > 3) {
self.hour   = [self.pickerView selectedRowInComponent:3];
}
if (self.rows > 4) {
self.minute   = [self.pickerView selectedRowInComponent:4];
}

NSLog(@"%ld-%ld-%ld %ld:%ld",(long)self.year,(long)self.month,(long)self.day,(long)self.hour,(long)self.minute);
}

#pragma mark - --- setters 属性 ---

- (void)setYearLeast:(NSInteger)yearLeast
{
_yearLeast = yearLeast;
}

- (void)setYearSum:(NSInteger)yearSum
{
_yearSum = yearSum;
}
#pragma mark - --- getters 属性 ---


@end

```



STPickerView.h 
```base
#import <UIKit/UIKit.h>

NS_ASSUME_NONNULL_BEGIN

typedef NS_ENUM(NSInteger, STPickerContentMode) {
STPickerContentModeBottom, // 1.选择器在视图的下方
STPickerContentModeCenter  // 2.选择器在视图的中间
};

@interface STPickerView : UIButton


- (instancetype)initWithRow:(NSInteger )rows;


/** 1.内部视图 */
@property (nonatomic, strong) UIView *contentView;
/** 2.边线,选择器和上方tool之间的边线 */
@property (nonatomic, strong)UIView *lineView;
/** 3.选择器 */
@property (nonatomic, strong)UIPickerView *pickerView;
/** 4.左边的按钮 */
@property (nonatomic, strong)UIButton *buttonLeft;
/** 5.右边的按钮 */
@property (nonatomic, strong)UIButton *buttonRight;
/** 6.标题label */
@property (nonatomic, strong)UILabel *labelTitle;
/** 7.下边线,在显示模式是STPickerContentModeCenter的时候显示 */
@property (nonatomic, strong)UIView *lineViewDown;
/** 8.上方按钮 */
@property (nonatomic, strong) UIView *btnView;


/** 1.标题，default is nil */
@property(nullable, nonatomic,copy) NSString          *title;
/** 2.字体，default is nil (system font 17 plain) */
@property(null_resettable, nonatomic,strong) UIFont   *font;
/** 3.字体颜色，default is nil (text draws black) */
@property(null_resettable, nonatomic,strong) UIColor  *titleColor;
/** 4.按钮边框颜色颜色，default is RGB(205, 205, 205) */
@property(null_resettable, nonatomic,strong) UIColor  *borderButtonColor;
/** 5.选择器的高度，default is 240 */
@property (nonatomic, assign)CGFloat heightPicker;
/** 6.视图的显示模式 */
@property (nonatomic, assign)STPickerContentMode contentMode;

@property (nonatomic, assign)NSInteger rows;



/**
*  5.创建视图,初始化视图时初始数据
*/
- (void)setupUI;

/**
*  6.确认按钮的点击事件
*/
- (void)selectedOk;

/**
*  7.显示
*/
- (void)show;

- (void)showWithBtnArray:(NSArray *)btnArr;
/**
*  8.移除
*/
- (void)remove;

@end
NS_ASSUME_NONNULL_END

```


STPickerView.m
```base

#define RGB(r, g, b) [UIColor colorWithRed:(r)/255.0 green:(g)/255.0 blue:(b)/255.0 alpha:1.0]
#define RGBA(r, g, b,a) [UIColor colorWithRed:(r)/255.0 green:(g)/255.0 blue:(b)/255.0 alpha:a]
#import "STPickerView.h"

@implementation STPickerView

#pragma mark - --- init 视图初始化 ---
- (instancetype)initWithRow:(NSInteger )rows
{
self = [super init];
if (self) {
_rows = rows;
[self setupDefault];
[self setupUI];
}
return self;
}

- (void)setupDefault
{
// 1.设置数据的默认值
_title             = nil;
_font              = [UIFont systemFontOfSize:15];
_titleColor        = [UIColor blackColor];
_borderButtonColor = RGB(205, 205, 205);
_heightPicker      = 240;
_contentMode       = STPickerContentModeBottom;

// 2.设置自身的属性
self.bounds = [UIScreen mainScreen].bounds;
self.backgroundColor = RGBA(0, 0, 0, 102.0/255);
self.layer.opacity = 0.0;
[self addTarget:self action:@selector(remove) forControlEvents:UIControlEventTouchUpInside];

// 3.添加子视图
[self addSubview:self.contentView];
[self.contentView addSubview:self.lineView];
[self.contentView addSubview:self.pickerView];
[self.contentView addSubview:self.buttonLeft];
[self.contentView addSubview:self.buttonRight];
[self.contentView addSubview:self.labelTitle];
[self.contentView addSubview:self.lineViewDown];
[self addSubview:self.btnView];
}

- (void)setupUI
{



}

- (void)layoutSubviews
{
[super layoutSubviews];

if (self.contentMode == STPickerContentModeBottom) {
}else {
self.buttonLeft.y = self.lineViewDown.bottom + 5;
self.buttonRight.y = self.lineViewDown.bottom + 5;
}
}

#pragma mark - --- delegate 视图委托 ---

#pragma mark - --- event response 事件相应 ---

- (void)selectedOk
{
[self remove];
}

- (void)selectedCancel
{
[self remove];
}

#pragma mark - --- private methods 私有方法 ---


- (void)show
{
[[UIApplication sharedApplication].keyWindow addSubview:self];
[self setCenter:[UIApplication sharedApplication].keyWindow.center];
[[UIApplication sharedApplication].keyWindow bringSubviewToFront:self];

if (self.contentMode == STPickerContentModeBottom) {
CGRect frameContent =  self.contentView.frame;
frameContent.origin.y -= self.contentView.height;
[UIView animateWithDuration:0.3 delay:0 options:UIViewAnimationOptionCurveEaseOut animations:^{
[self.layer setOpacity:1.0];
self.contentView.frame = frameContent;
} completion:^(BOOL finished) {
}];
}else {
CGRect frameContent =  self.contentView.frame;
frameContent.origin.y -= (kScreenHeight+self.contentView.height)/2;
[UIView animateWithDuration:0.3 delay:0 options:UIViewAnimationOptionCurveEaseOut animations:^{
[self.layer setOpacity:1.0];
self.contentView.frame = frameContent;
} completion:^(BOOL finished) {
}];
}
}

- (void)showWithBtnArray:(NSArray *)btnArr
{
[[UIApplication sharedApplication].keyWindow addSubview:self];
[self setCenter:[UIApplication sharedApplication].keyWindow.center];
[[UIApplication sharedApplication].keyWindow bringSubviewToFront:self];
_btnView.hidden = NO;
CGFloat btnW = (kScreenWidth - btnArr.count - 1)/btnArr.count;
for (int i = 0; i < btnArr.count; i++) {
UIButton *btn = [UIButton buttonWithType:UIButtonTypeCustom];
btn.frame = CGRectMake(btnW * i + 1, 0, btnW, 34);
[btn setTitle:btnArr[i] forState:UIControlStateNormal];
[btn setTitleColor:rgb(33, 33, 33) forState:UIControlStateNormal];
btn.tag = i;
[btn addTarget:self action:@selector(btnAction:) forControlEvents:UIControlEventTouchUpInside];

[self.btnView addSubview:btn];
}
if (self.contentMode == STPickerContentModeBottom) {
CGRect frameContent =  self.contentView.frame;
frameContent.origin.y -= self.contentView.height;
[UIView animateWithDuration:0.3 delay:0 options:UIViewAnimationOptionCurveEaseOut animations:^{
[self.layer setOpacity:1.0];
self.contentView.frame = frameContent;
} completion:^(BOOL finished) {
}];
}else {
CGRect frameContent =  self.contentView.frame;
frameContent.origin.y -= (kScreenHeight+self.contentView.height)/2;
[UIView animateWithDuration:0.3 delay:0 options:UIViewAnimationOptionCurveEaseOut animations:^{
[self.layer setOpacity:1.0];
self.contentView.frame = frameContent;
} completion:^(BOOL finished) {
}];
}
}

- (void)btnAction:(UIButton *)btn{
_rows = btn.tag + 1;
[self setupUI];
}


- (void)remove
{
if (self.contentMode == STPickerContentModeBottom) {
CGRect frameContent =  self.contentView.frame;
frameContent.origin.y += self.contentView.height;
[UIView animateWithDuration:0.3 delay:0 options:UIViewAnimationOptionCurveEaseOut animations:^{
[self.layer setOpacity:0.0];
self.contentView.frame = frameContent;
} completion:^(BOOL finished) {
[self removeFromSuperview];
}];
}else {
CGRect frameContent =  self.contentView.frame;
frameContent.origin.y += (kScreenHeight+self.contentView.height)/2;
[UIView animateWithDuration:0.3 delay:0 options:UIViewAnimationOptionCurveEaseOut animations:^{
[self.layer setOpacity:0.0];
self.contentView.frame = frameContent;
} completion:^(BOOL finished) {
[self removeFromSuperview];
}];
}
}

#pragma mark - --- setters 属性 ---

- (void)setTitle:(NSString *)title
{
_title = title;
[self.labelTitle setText:title];
}

- (void)setFont:(UIFont *)font
{
_font = font;
[self.buttonLeft.titleLabel setFont:font];
[self.buttonRight.titleLabel setFont:font];
[self.labelTitle setFont:font];
}

- (void)setTitleColor:(UIColor *)titleColor
{
_titleColor = titleColor;
[self.labelTitle setTextColor:titleColor];
[self.buttonLeft setTitleColor:titleColor forState:UIControlStateNormal];
[self.buttonRight setTitleColor:titleColor forState:UIControlStateNormal];
}

- (void)setBorderButtonColor:(UIColor *)borderButtonColor
{
_borderButtonColor = borderButtonColor;
//    [self.buttonLeft addBorderColor:borderButtonColor];
//    [self.buttonRight addBorderColor:borderButtonColor];
}

- (void)setHeightPicker:(CGFloat)heightPicker
{
_heightPicker = heightPicker;
self.contentView.height = heightPicker;
}

- (void)setContentMode:(STPickerContentMode)contentMode
{
_contentMode = contentMode;
if (contentMode == STPickerContentModeCenter) {
self.contentView.height += 44;
}
}
#pragma mark - --- getters 属性 ---
- (UIView *)contentView
{
if (!_contentView) {
CGFloat contentX = 0;
CGFloat contentY = kScreenHeight;
CGFloat contentW = kScreenWidth;
CGFloat contentH = self.heightPicker;
_contentView = [[UIView alloc]initWithFrame:CGRectMake(contentX, contentY, contentW, contentH)];
[_contentView setBackgroundColor:[UIColor whiteColor]];
}
return _contentView;
}

- (UIView *)btnView{
if (!_btnView){
_btnView = [[UIView alloc] initWithFrame:CGRectMake(0, kScreenHeight - self.heightPicker - 35, self.contentView.width, 35)];
_btnView.backgroundColor = [UIColor whiteColor];
UIView *line = [[UIView alloc] initWithFrame:CGRectMake(0, 34, kScreenWidth, 1)];
line.backgroundColor = rgb(240, 240, 240);
[_btnView addSubview:line];
_btnView.hidden = YES;
}
return _btnView;
}

- (UIView *)lineView
{
if (!_lineView) {
CGFloat lineX = 0;
CGFloat lineY = 44;
CGFloat lineW = self.contentView.width;
CGFloat lineH = 0.5;
_lineView = [[UIView alloc]initWithFrame:CGRectMake(lineX, lineY, lineW, lineH)];
[_lineView setBackgroundColor:self.borderButtonColor];
}
return _lineView;
}

- (UIPickerView *)pickerView
{
if (!_pickerView) {
CGFloat pickerW = self.contentView.width;
CGFloat pickerH = self.contentView.height - self.lineView.bottom;
CGFloat pickerX = 0;
CGFloat pickerY = self.lineView.bottom;
_pickerView = [[UIPickerView alloc]initWithFrame:CGRectMake(pickerX, pickerY, pickerW, pickerH)];
[_pickerView setBackgroundColor:[UIColor whiteColor]];
}
return _pickerView;
}

- (UIButton *)buttonLeft
{
if (!_buttonLeft) {
CGFloat leftW = 36;
CGFloat leftH = self.lineView.top - 10;
CGFloat leftX = 16;
CGFloat leftY = (self.lineView.top - leftH) / 2;
_buttonLeft = [[UIButton alloc]initWithFrame:CGRectMake(leftX, leftY, leftW, leftH)];
[_buttonLeft setTitle:@"取消" forState:UIControlStateNormal];
[_buttonLeft setTitleColor:self.titleColor forState:UIControlStateNormal];
//        [_buttonLeft addBorderColor:self.borderButtonColor];
[_buttonLeft.titleLabel setFont:self.font];
[_buttonLeft addTarget:self action:@selector(selectedCancel) forControlEvents:UIControlEventTouchUpInside];
}
return _buttonLeft;
}

- (UIButton *)buttonRight
{
if (!_buttonRight) {
CGFloat rightW = self.buttonLeft.width;
CGFloat rightH = self.buttonLeft.height;
CGFloat rightX = self.contentView.width - rightW - self.buttonLeft.x;
CGFloat rightY = self.buttonLeft.y;
_buttonRight = [[UIButton alloc]initWithFrame:CGRectMake(rightX, rightY, rightW, rightH)];
[_buttonRight setTitle:@"确定" forState:UIControlStateNormal];
[_buttonRight setTitleColor:self.titleColor forState:UIControlStateNormal];
//        [_buttonRight addBorderColor:self.borderButtonColor];
[_buttonRight.titleLabel setFont:self.font];
[_buttonRight addTarget:self action:@selector(selectedOk) forControlEvents:UIControlEventTouchUpInside];
}
return _buttonRight;
}

- (UILabel *)labelTitle
{
if (!_labelTitle) {
CGFloat titleX = self.buttonLeft.right + 5;
CGFloat titleY = 0;
CGFloat titleW = self.contentView.width - titleX * 2;
CGFloat titleH = self.lineView.top;
_labelTitle = [[UILabel alloc]initWithFrame:CGRectMake(titleX, titleY, titleW, titleH)];
[_labelTitle setTextAlignment:NSTextAlignmentCenter];
[_labelTitle setTextColor:self.titleColor];
[_labelTitle setFont:self.font];
_labelTitle.adjustsFontSizeToFitWidth = YES;
}
return _labelTitle;
}

- (UIView *)lineViewDown
{
if (!_lineViewDown) {
CGFloat lineX = 0;
CGFloat lineY = self.pickerView.bottom;
CGFloat lineW = self.contentView.width;
CGFloat lineH = 0.5;
_lineViewDown = [[UIView alloc]initWithFrame:CGRectMake(lineX, lineY, lineW, lineH)];
[_lineViewDown setBackgroundColor:self.borderButtonColor];
}
return _lineViewDown;
}

@end

```
