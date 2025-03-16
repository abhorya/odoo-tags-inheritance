# Odoo Custom Tagging System | نظام تصنيف مخصص لـ Odoo

## Overview | نظرة عامة
This module extends Odoo's CRM tagging system to allow structured categorization of customers, vendors, and products using `crm.tag`. It ensures:
- Unified tagging for **customers, vendors, and products**.
- Role-based **access control** for different tags.
- **Automatic tag assignment** based on user permissions.
- **Filtering and search** improvements.

يعمل هذا الموديول على توسيع نظام التصنيفات في Odoo CRM للسماح بتصنيف العملاء والموردين والمنتجات بطريقة منظمة باستخدام `crm.tag`. يضمن:
- توحيد التصنيفات لكل من **العملاء، الموردين، والمنتجات**.
- **التحكم في الوصول بناءً على الأدوار** لكل تصنيف.
- **تعيين التصنيفات تلقائيًا** بناءً على أذونات المستخدم.
- **تحسين البحث والتصفية**.

## Features | الميزات
### 1️⃣ **Extended Partner & Product Models | توسيع نماذج الشركاء والمنتجات**
- إضافة `company_tag` إلى `res.partner` (العملاء والموردين).
- إضافة `company_tag` إلى `product.template` (المنتجات).
- التصنيفات مأخوذة من `crm.tag` ومقسمة إلى:
  - `Customer | عميل`
  - `Vendor | مورد`
  - `Product | منتج`

### 2️⃣ **User Access Control | التحكم في وصول المستخدمين**
- يمتلك المستخدمون التصنيفات المسموح بها:
  - `allowed_customer_tags` (تصنيفات العملاء المسموح بها)
  - `allowed_vendor_tags` (تصنيفات الموردين المسموح بها)
  - `allowed_product_tags` (تصنيفات المنتجات المسموح بها)
- لا يمكن للمستخدمين رؤية إلا السجلات **المتوافقة مع تصنيفاتهم المسموح بها**.

### 3️⃣ **Record Access Restrictions | تقييد الوصول إلى السجلات**
- **العملاء والموردون:** الوصول مقيد وفقًا لـ `allowed_customer_tags` و `allowed_vendor_tags`.
- **المنتجات:** الوصول مقيد وفقًا لـ `allowed_product_tags`.
- **تصنيفات المنتجات:** المستخدمون لا يمكنهم رؤية أو تعديل تصنيفات المنتجات إلا إذا كانت ضمن تصنيفاتهم المسموح بها.

### 4️⃣ **Auto-Assign Default Tags | تعيين التصنيفات تلقائيًا**
- عند إنشاء **عميل أو مورد**، يتم تعيين أول `allowed_customer_tags` أو `allowed_vendor_tags` تلقائيًا.
- عند إنشاء **منتج**، يتم تعيين أول `allowed_product_tags` تلقائيًا.

### 5️⃣ **UI Enhancements & Filtering | تحسينات الواجهة والتصفية**
- **قائمة الإعدادات في CRM:** `CRM → الإعدادات → التصنيفات`.
- **شاشات العملاء والموردين والمنتجات:** تمت إضافة `company_tag`.
- **إعدادات المستخدم:** يمكن للمستخدمين إدارة التصنيفات المتاحة لهم.
- **تصنيفات المنتجات:** تم توارث `product.product_tag_form_view`.
- **تحسينات البحث والتصفية:** يمكن للمستخدمين تصفية السجلات حسب `company_tag`.

## Installation & Usage | التثبيت والاستخدام
1. **قم بتثبيت الموديول**.
2. قم بتكوين **أذونات تصنيفات المستخدم** من `الإعدادات → المستخدمون والشركات → المستخدمون`.
3. قم بتعيين **تصنيفات للعملاء، الموردين، والمنتجات**.
4. لن يتمكن المستخدمون من رؤية إلا البيانات المتوافقة مع تصنيفاتهم المسموح بها.

## Security & Permissions | الأمان والصلاحيات
- **ملف الأمان CSV:** يحدد قيود القراءة/الكتابة لكل نموذج.
- **قواعد السجلات:** تمنع الوصول غير المصرح به إلى السجلات خارج التصنيفات المسموح بها للمستخدم.

## Future Enhancements | التحسينات المستقبلية
- **دعم تعدد الشركات:** السماح للمستخدمين بالتبديل بين التصنيفات وفقًا للشركة.
- **لوحة تحكم مخصصة:** عرض بصري للسجلات المصنفة حسب `company_tag`.

## Credits | الشكر والتقدير
- Developed by **Sabry Youssef | صبري يوسف**

---
This module ensures **better data organization, access control, and usability** across Odoo! | يضمن هذا الموديول **تنظيمًا أفضل للبيانات، وتحكمًا محسّنًا في الوصول، وتجربة استخدام أفضل** داخل Odoo!

