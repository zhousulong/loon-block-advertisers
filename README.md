# Loon BlockAdvertisers (广告平台拦截器 - 放行 Google & Yandex)

基于 [可莉🅥 的广告平台拦截器 (BlockAdvertisers.lpx)](https://hub.kelee.one) 定制，**移除了 Google 和 Yandex 旗下的所有广告及统计域名拦截规则**，避免在使用代理或广告拦截时误伤 Google 和 Yandex 平台的正常广告展示与业务服务。

---

## 插件订阅地址 (Loon Plugin)

在 Loon 的「配置」->「插件」中添加外部插件：

### GitHub Raw 直接地址
```text
https://raw.githubusercontent.com/zhousulong/loon-block-advertisers/main/BlockAdvertisers.lpx
```

### jsDelivr CDN 加速地址（国内推荐）
```text
https://cdn.jsdelivr.net/gh/zhousulong/loon-block-advertisers@main/BlockAdvertisers.lpx
```

---

## 过滤策略说明

上游规则源地址：`https://kelee.one/Tool/Loon/Lpx/BlockAdvertisers.lpx`

已剔除的 Google / Yandex 广告及分析域名列表：
- `app-analytics-services.com`
- `odm.app-ads-services.com`
- `firebaselogging-pa.googleapis.com`
- `firebaseinappmessaging.googleapis.com`
- `fundingchoicesmessages.google.com`
- `doubleclick.net`
- `doubleclick-cn.net`
- `googlesyndication.com`
- `googlesyndication-cn.com`
- 以及任何后续上游可能新增的 `yandex` / `appmetrica` 规则

---

## 本地更新与自动化

运行更新脚本拉取上游最新规则并自动过滤：

```bash
python3 update.py
```

> **注意**：上游 `kelee.one` 配置了 Cloudflare WAF，必须使用特定的 Loon `User-Agent` 标头请求，`update.py` 已内置该请求头。
