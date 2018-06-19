
/**
 *  var：声明全局变量.
 *  let：声明块级变量，即局部变量.
 *  const：用于声明常量.
 */ 
//获取当前的app变量
const app = getApp()
const currentPage = getCurrentPages()
const currentRoute = Page.prototype.route

Page({

  /**
   * 页面的初始数据
   */
  data: {
    text:'init data',
    num:12,
    array1: [{'msg': '1' }, { 'msg':'2'}],
    array2: [{'msg':'12',"code":'23'},{'msg':'32',"code":'34'}],
    object:{
      'text':'我是占位的view'
    }
  },

  /**
   * Change normal data btn 的点击, 并切换tabBar
   */ 
  clickBtn: function () {
    this.data.num = 15
    this.setData({
      num : this.data.num
    })
    wx.switchTab({
      url: '../index/index',
    })
  },
  /**
   * 点我: 涉及到navigationBar页面跳转
   */
  ViewTap:function() {
    console.log('你点到我了,赔钱')
    /**
     * 导航跳转2种方式：navigateTo 和 redirectTo
     */ 
    wx.navigateTo({
      url: 'minehome/minehome',
    })
    wx.redirectTo({//重新指向某路由后页面，路有前的页面会被销毁，执行onUnload
      url: 'minehome/minehome',
    })
  },

  /**
   * 点我调转到任何page:reLaunch 路由前页面是会被释放掉
   */ 
  JumpAnyPage:function() {
    wx.reLaunch({//重新创建某路由后页面，路有前的页面会被销毁，执行onUnload
      // url: 'minehome/minehome',
      url: "../logs/logs"
    })
  },

  /**
   * 生命周期函数--监听页面加载：获取页面的参数
   */
  onLoad: function (options) {
    this.setData({
      text:'我更新数据了',
      array1:[{'msg':'我是来更新数组的'},{'msg':'对，我就是更新数组1的'}],
      array2:[{'msg':'这会有啥呢','code':'404'},{'msg':'这不会有啥','code':'303'}]
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    console.log('mine页面被干掉了')
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    return {
      title:"我是标题",
      path:"/page/user?id=123"
    }
  },

  /**
   * 页面滚动时，发生响应
   */ 
  onPageScroll: function () {
    // Do something when page scroll
  },

  /**
   * 点击tabItem执行
   */ 
  onTabItemTap(item) {
    console.log(item.index)
    console.log(item.pagePath)
    console.log(item.text)
  },


})