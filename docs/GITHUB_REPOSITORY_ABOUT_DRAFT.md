# GitHub repository About fields — proposed copy

The GitHub connector currently supports reading repository metadata and editing repository files, but **not editing repository About descriptions, homepage URLs, profile biography, or pinned repositories**. These entries are prepared for manual update in GitHub repository Settings/About.

| Repository | Suggested short description |
|---|---|
| `smart-trader-Pro` | منصة لإدارة الجهات والأصناف والأسعار وتكاليف الحمولة، بتخزين محلي ومزامنة اختيارية. |
| `Rakan-Image-Studio` | مشروع Rakan Image Studio — تفاصيل الوظائف غير موثقة بعد؛ يلزم تحديد النطاق قبل كتابة وصف دقيق. |
| `Abdullah-Almkhlafi-Portfolio-Clean` | موقع شخصي بواجهة React وخادم Node.js وMySQL، مع إدارة محتوى ووسائط ونشر على Hostinger. |
| `alrashid-boutique` | متجر بوتيك الراشد: واجهة عربية للمنتجات والتصنيفات والسلة والطلبات ولوحة الإدارة. |
| `Professional-AI-Skills-Hub` | مكتبة مهارات احترافية لوكلاء الذكاء الاصطناعي، مع مراجعات أمان وجودة واختبارات موثقة. |

## Profile setup

GitHub profile README is displayed when the account owns a **public** repository named exactly `aalmkhlafi77-sudo`, with a root `README.md`. Such a repository was **not present** in the accessible list of 27 repositories at audit time. The connector cannot create repositories or edit account appearance. Copy `docs/GITHUB_PROFILE_README_DRAFT.md` into the root README of that profile repository after creating it.

Do not claim these About fields or profile settings were applied automatically.
