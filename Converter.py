# File has 1917 lines, 8842 words, and 76895 characters.
class Converter:
    cases = {
        # A : المزيد بحرف واحد
        # B : المزيد بحرفين
        # C : المزيد بثلاثة حروف
        # Main A Case1
        'case_a_1_1': 'الصحيح السالم من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_1w': 'المثال الواوي من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_1y': 'المثال اليائي من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_2': 'الصحيح المضعف من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_3': 'الصحيح مهموز الفاء من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_4': 'الصحيح مهموز اللام من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_5': 'المعتل الاجوف بالألف من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_6a': 'المعتل الناقص بالالف من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_6f': 'المعتل اللفيف (واو و الف [ الفاء واللام ]) من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_6e': 'المعتل اللفيف (واو و الف [ العين واللام ]) من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        'case_a_1_7': 'الناقص بالالف مهموز الفاء من أَفْعَل مُفْعِل [مزيد بحرف (الألف)]',
        # Main A Case2
        'case_a_2_1': 'الصحيح السالم من فَعَّل مُفَعِّل [مزيد بحرف (تضعيف العين)]',
        'case_a_2_1d': 'الصحيح المضعف من فَعَّل مُفَعِّل [مزيد بحرف (تضعيف العين)]',
        'case_a_2_1a': 'الصحيح مهموز الفاء من فَعَّل مُفَعِّل [مزيد بحرف (تضعيف العين)]',
        'case_a_2_1jy': 'المعتل الاجوف بالياء من فَعَّل مُفَعِّل [مزيد بحرف (تضعيف العين)]',
        'case_a_2_1jw': 'المعتل الاجوف بالواو من فَعَّل مُفَعِّل [مزيد بحرف (تضعيف العين)]',
        'case_a_2_2a': 'الناقص بالالف من فَعَّل مُفَعِّل [مزيد بحرف (تضعيف العين)]',
        'case_a_2_2wa': 'اللفيف بالواو والالف من فَعَّل مُفَعِّل [مزيد بحرف (تضعيف العين)]',
        # Main A Case3
        'case_a_3_1': 'الصحيح السالم من فَاعَل مُفَاعِل [مزيد بحرف (ألف المد بعد الفاء)]',
        'case_a_3_1w': 'المعتل المثال الواوي من فَاعَل مُفَاعِل [مزيد بحرف (ألف المد بعد الفاء)]',
        'case_a_3_2': 'الصحيح المضعف من فَاعَل مُفَاعِل [مزيد بحرف (ألف المد بعد الفاء)]',
        'case_a_3_3': 'المعتل الناقص بالألف من فَاعَل مُفَاعِل [مزيد بحرف (ألف المد بعد الفاء)]',
        # Main B Case1
        'case_b_1_1': 'الصحيح السالم من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        'case_b_1_2': 'الصحيح السالم (إبدال) من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        'case_b_1_3': 'الصحيح المضعف من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        'case_b_1_4': 'الصحيح مهموز الفاء من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        'case_b_1_5': 'الصحيح مهموز الفاء (إبدال) من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        'case_b_1_6': 'المعتل الأجوف بالألف من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        'case_b_1_7': 'المعتل الناقص بالألف من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        'case_b_1_8': 'المعتل اللفيف (إبدال) من اِفْتَعَل مُفْتَعِل [مزيد بحرفين (الألف والتاء)]',
        # Main B Case2
        'case_b_2_1': 'الصحيح السالم من اِنْفَعَل مُنْفَعِل [مزيد بحرفين(الألف والنون)]',
        'case_b_2_2': 'الصحيح المضعف من اِنْفَعَل مُنْفَعِل [مزيد بحرفين(الألف والنون)]',
        # Main B Case3
        'case_b_3_1': 'الصحيح السالم من تَفَعَّل مُتَفَعِّل [مزيد بحرفين (التاء وتضعيف العين)]',
        'case_b_3_1w': 'المعتل (المثال الواوي) من تَفَعَّل مُتَفَعِّل [مزيد بحرفين (التاء وتضعيف العين)]',
        'case_b_3_2': 'الصحيح السالم (إبدال) من تَفَعَّل مُتَفَعِّل [مزيد بحرفين (التاء وتضعيف العين)]',
        'case_b_3_3a': 'المعتل الناقص بالألف من تَفَعَّل مُتَفَعِّل [مزيد بحرفين (التاء وتضعيف العين)]',
        'case_b_3_3w': 'المعتل اللفيف من تَفَعَّل مُتَفَعِّل [مزيد بحرفين (التاء وتضعيف العين)]',
        # Main B Case4
        'case_b_4_1': 'الصحيح السالم من تَفَاعَل مُتَفَاعِل [مزيد بحرفين (التاء وألف المد بعد الفاء)]',
        'case_b_4_1w': 'الأجوف الواوي من تَفَاعَل مُتَفَاعِل [مزيد بحرفين (التاء وألف المد بعد الفاء)]',
        'case_b_4_2': 'المعتل الناقص بالألف من تَفَاعَل مُتَفَاعِل [مزيد بحرفين (التاء وألف المد بعد الفاء)]',
        # Main B case5
        'case_b_5_1': 'الصحيح السالم من اِفْعَلّ , مُفْعَلّ [مزيد بحرفين (الألف وتضعيف اللام)]',
        'case_b_5_1w': 'المعتل الأجوف الواوي من اِفْعَلّ , مُفْعَلّ [مزيد بحرفين (الألف وتضعيف اللام)]',
        # Main C case1
        'case_c_1_1': 'الصحيح السالم من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        'case_c_1_1af': 'الصحيح المهموز الفاء من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        'case_c_1_1al': 'الصحيح المهموز اللام من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        'case_c_1_1y': 'المعتل (المثال اليائي) من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        'case_c_1_2': 'الصحيح المضعف من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        'case_c_1_3': 'المعتل الاجوف بالالف من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        'case_c_1_4': 'المعتل الناقص بالالف من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        'case_c_1_4f': 'المعتل اللفيف (الواو والالف) من اِسْتَفْعَل مُسْتَفْعِل [مزيد بثلاثة أحرف (الألف والسين والتاء)]',
        # Main C case2
        'case_c_2_1': 'الصحيح السالم من اِفْعَالّ , مُفْعَالّ [مزيد بثلاثة أحرف (الألف والألف بعد العين وتضعيف اللام)]',
    }

    C1 = [
          'ب',
          'ت',
          'ث',
          'ج',
          'ح',
          'خ',
          'د',
          'ذ',
          'ر',
          'ز',
          'س',
          'ش',
          'ص',
          'ض',
          'ط',
          'ظ',
          'ع',
          'غ',
          'ف',
          'ق',
          'ك',
          'ل',
          'ن',
          'ه',
          'ھ',
          'ل',
          'م'
          ]
    C2 = C1.copy()
    C3 = C1.copy()

    constants = {
        # BX = أحرف زيادة
        # همزة القطع
        'B0': 'أ',
        # همزة الوصل
        'B1': 'ا',
        'aa': 'ا',
        'a2': 'ى',
        # السين
        'B2': 'س',
        # التاء
        'B3': 'ت',
        # النون
        'B4': 'ن',
        # همزة على السطر
        'E0': '\u0674',
        # همزة على الف
        'E1': 'أ',
        # همزة على ياء
        'E2': 'ئ',
        # همزة على الواو
        'E3': 'ؤ',
        # ميم
        'm': 'م',
        # واو
        'w': 'و',
        # ياء
        'y': 'ي',
        # الالف الممدودة
        '(aa)': 'آ',
        # ال التعريف
        'AL': 'ال'
    }
    tashkeel = {
        'na': '\u064b',  # تنوين الفتح
        'nu': '\u064c',  # تنوين الضم
        'ni': '\u064d',  # تنوين الكسر
        'd': '\u0651',  # الشدة
        'a': '\u064E',  # الفتحة
        'u': '\u064F',  # الضمة
        'i': '\u0650',  # الكسرة
        's': '\u0652',  # السكون

    }
# case_b_5_1
# case_b_1_3
    roots = {
        'اعترّ': 'عرر',
        'اقترّ': 'قرر'
    }

    def __ini__(self):
        pass

    def get_root(self, word):
        return self.roots.get(word, word)

    def clean(self, word):
        for t in self.tashkeel.values():
            word = word.replace(t, '')
        return word

    def clean2(self, word):
        final_word = word.strip()
        for t in self.tashkeel.values():
            final_word = final_word.replace(t, '', len(word))
        final_word = list(final_word)
        final_word.append(word[-1])
        return ''.join(final_word)

    def case_a_1_1(self, word):
        # أيقن
        # أصلح
        # أوهن
        C1 = self.C1.copy()
        C1.append('ي')
        C1.append('و')
        word = self.clean(word)
        if(len(word) != 4):
            return None
        else:
            if(word[0] == self.constants['B0']):
                if(word[1] in C1):
                    if(word[2] in self.C2):
                        if(word[3] in self.C3):
                            return self.generate_case_a_1_1_word(word)

    def case_a_1_1_v2(self, word):
        # أيقن
        # أصلح
        # أوهن
        C1 = self.C1.copy()
        C1.append('ي')
        C1.append('و')
        # word = self.clean(word)

        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['B0']):
                    if(word[1] in C1):
                        if(word[2] in self.C2):
                            if(word[3] in self.C3 and word[3]):
                                return True

        def check2(word):
            if(len(word) == 7):
                if(word[0] == self.constants['B0'] and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in C1 and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] in self.C2 and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C3 and word[6]):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_1_1_word(word)

    def case_a_1_2(self, word):
        # أتمّ
        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['B0']):
                    if(word[1] in self.C1):
                        if(word[2] in self.C2):
                            if(word[3] == self.tashkeel['d']):
                                return True

        def check2(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B0'] and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['a']):  # noqa
                        if(word[4] in self.C2):
                            if(word[5] == self.tashkeel['d']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_1_2_word(word)

    def case_a_1_3(self, word):
        # آمن
        def check1(word):
            if(len(word) == 3):
                if(word[0] == self.constants['(aa)']):
                    if(word[1] in self.C1):
                        if(word[2] in self.C2):
                            return True

        def check2(word):
            if(len(word) == 4):
                if(word[0] == self.constants['(aa)']):
                    if(word[1] in self.C1 and word[2] == self.tashkeel['a']):
                        if(word[3] in self.C2):
                            return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_1_3_word(word)

    def case_a_1_4(self, word):
        # أنشأ
        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['B0']):
                    if(word[1] in self.C1):
                        if(word[2] in self.C2):
                            if(word[3] == self.constants['E1']):
                                return True

        def check2(word):
            if(len(word) == 7):
                if(word[0] == self.constants['B0'] and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['s']):
                        if(word[4] in self.C2 and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] == self.constants['E1']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_1_4_word(word)

    def case_a_1_5(self, word):
        # أغار
        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['B0']):
                    if(word[1] in self.C1):
                        if(word[2] == self.constants['aa']):
                            if(word[3] in self.C3):
                                return True

        def check2(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B0'] and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['a']):
                        if(word[4] == self.constants['aa']):
                            if(word[5] in self.C3):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_1_5_word(word)

    def case_a_1_6(self, word):
        # أخزى
        C1 = self.C1.copy()
        C2 = self.C2.copy()
        C1.append('و')
        C2.append('و')

        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['B0']):
                    if(word[1] in C1):
                        if(word[2] in C2):
                            if(word[3] == self.constants['a2']):
                                return True

        def check2(word):
            if(len(word) == 7):
                if(word[0] == self.constants['B0'] and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in C1 and word[3] == self.tashkeel['s']):
                        if(word[4] in C2 and word[5] == self.tashkeel['a']):
                            if(word[6] == self.constants['a2']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_1_6_word(word)

    def case_a_1_7(self, word):
        # آتى
        def check1(word):
            if(len(word) == 3):
                if(word[0] == self.constants['(aa)']):
                    if(word[1] in self.C1):
                        if(word[2] == self.constants['a2']):
                            return True

        def check2(word):
            if(len(word) == 4):
                if(word[0] == self.constants['(aa)']):
                    if(word[1] in self.C1 and word[2] == self.tashkeel['a']):
                        if(word[3] == self.constants['a2']):
                            return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_1_7_word(word)

    def case_a_2_1(self, word):
        # أذن
        # سوم
        # طفف
        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['E1'] or word[0] in self.C1):
                    if(word[1] in self.C2 or word[1] == self.constants['w'] or word[1] == self.constants['y']):  # noqa
                        if(word[2] == self.tashkeel['d']):
                            if(word[3] in self.C3):
                                return True

        def check2(word):
            word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
            if(len(word) == 6):
                if((word[0] == self.constants['E1'] or word[0] in self.C1) and word[1] == self.tashkeel['a']):  # noqa
                    if((word[2] in self.C2 or word[2] == self.constants['w'] or word[2] == self.constants['y']) and word[3] == self.tashkeel['d']):  # noqa
                        if(word[4] == self.tashkeel['a']):
                            if(word[5] in self.C3):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_2_1_word(word)

    def case_a_2_2(self, word):
        # صلى
        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['w'] or word[0] in self.C1):
                    if(word[1] in self.C2):  # noqa
                        if(word[2] == self.tashkeel['d']):
                            if(word[3] == self.constants['a2']):
                                return True

        def check2(word):
            word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
            if(len(word) == 6):
                if((word[0] == self.constants['w'] or word[0] in self.C1) and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in self.C2 and word[3] == self.tashkeel['d']):  # noqa
                        if(word[4] == self.tashkeel['a']):
                            if(word[5] == self.constants['a2']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_2_2_word(word)

    def case_a_3_1(self, word):
        # واقع نافق
        def check1(word):
            if(len(word) == 4):
                if(word[0] == self.constants['w'] or word[0] in self.C1):
                    if(word[1] == self.constants['aa']):  # noqa
                        if(word[2] in self.C2):
                            if(word[3] in self.C3):
                                return True

        def check2(word):
            if(len(word) == 6):
                if((word[0] == self.constants['w'] or word[0] in self.C1) and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] == self.constants['aa']):  # noqa
                        if(word[3] in self.C2 and word[4] == self.tashkeel['a']):  # noqa
                            if(word[5] in self.C3):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_3_1_word(word)

    def case_a_3_2(self, word):
        # ضارّ
        def check1(word):
            if(len(word) == 4):
                if(word[0] in self.C1):
                    if(word[1] == self.constants['aa']):  # noqa
                        if(word[2] in self.C2):
                            if(word[3] == self.tashkeel['d']):
                                return True

        def check2(word):
            if(len(word) == 5):
                if(word[0] in self.C1 and word[1] == self.tashkeel['a']):
                    if(word[2] == self.constants['aa']):  # noqa
                        if(word[3] in self.C2):
                            if(word[4] == self.tashkeel['d']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_3_2_word(word)

    def case_a_3_3(self, word):
        # نادى
        def check1(word):
            if(len(word) == 4):
                if(word[0] in self.C1):
                    if(word[1] == self.constants['aa']):  # noqa
                        if(word[2] in self.C2):
                            if(word[3] == self.constants['a2']):
                                return True

        def check2(word):
            if(len(word) == 6):
                if(word[0] in self.C1 and word[1] == self.tashkeel['a']):
                    if(word[2] == self.constants['aa']):  # noqa
                        if(word[3] in self.C2 and word[4] == self.tashkeel['a']):  # noqa
                            if(word[5] == self.constants['a2']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_a_3_3_word(word)

    def case_b_1_1(self, word):
        # اقتصد
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1):  # noqa
                        if(word[2] == self.constants['B3']):
                            if(word[3] in self.C2):
                                if(word[4] in self.C3):
                                    return True

        def check2(word):
            if(len(word) == 9):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C2 and word[7] == self.tashkeel['a']):  # noqa
                                if(word[8] in self.C3):
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_1_word(word)

    def case_b_1_2(self, word):
        # اتّخذ
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1 and word[2] == self.tashkeel['d']):  # noqa
                        if(word[3] in self.C2):
                            if(word[4] in self.C3):
                                return True

        def check2(word):
            if(len(word) == 8):
                word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['d'] and word[4] == self.tashkeel['a']):  # noqa
                        if(word[5] in self.C2 and word[6] == self.tashkeel['a']):  # noqa
                            if(word[7] in self.C3):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_2_word(word)

    # case_b_5_1
    def case_b_1_3(self, word):
        # اعترّ
        w_root = self.get_root(self.clean2(word))
        if(w_root[-1] != w_root[-2]):
            return None

        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1):  # noqa
                        if(word[2] == self.constants['B3']):
                            if(word[3] in self.C2 and word[4] == self.tashkeel['d']):  # noqa
                                return True

        def check2(word):
            if(len(word) == 9):
                word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C3 and word[7] == self.tashkeel['d'] and word[8] == self.tashkeel['a']):  # noqa
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_3_word(word)

    def case_b_1_4(self, word):
        # ائتفك
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] == self.constants['E2']):  # noqa
                        if(word[2] == self.constants['B3']):
                            if(word[3] in self.C2):  # noqa
                                if(word[4] in self.C3):
                                    return True

        def check2(word):
            if(len(word) == 9):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] == self.constants['E2'] and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C3 and word[7] == self.tashkeel['a']):  # noqa
                                if(word[8] in self.C3):
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_4_word(word)

    def case_b_1_5(self, word):
        # اتّكأ
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1 and word[2] == self.tashkeel['d']):  # noqa
                        if(word[3] in self.C2):
                            if(word[4] == self.constants['E1']):  # noqa
                                return True

        def check2(word):
            if(len(word) == 8):
                word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['d'] and word[4] == self.tashkeel['a']):  # noqa
                        if(word[5] in self.C2 and word[6] == self.tashkeel['a']):  # noqa
                            if(word[7] == self.constants['E1']):  # noqa
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_5_word(word)

    def case_b_1_6(self, word):
        # ارتاب
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1):  # noqa
                        if(word[2] == self.constants['B3']):
                            if(word[3] == self.constants['aa']):  # noqa
                                if(word[4] in self.C2):
                                    return True

        def check2(word):
            if(len(word) == 8):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] == self.constants['aa']):  # noqa
                                if(word[7] in self.C2):
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_6_word(word)

    def case_b_1_7(self, word):
        # اهتدى
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1):  # noqa
                        if(word[2] == self.constants['B3']):
                            if(word[3] in self.C2):  # noqa
                                if(word[4] == self.constants['a2']):
                                    return True

        def check2(word):
            if(len(word) == 9):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C2 and word[7] == self.tashkeel['a']):  # noqa
                                if(word[8] == self.constants['a2']):
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_7_word(word)

    def case_b_1_8(self, word):
        # اتقى
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1 and word[2] == self.tashkeel['d']):  # noqa
                        if(word[3] in self.C2):
                            if(word[4] == self.constants['a2']):
                                return True

        def check2(word):
            if(len(word) == 8):
                word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['d'] and word[4] == self.tashkeel['a']):  # noqa
                        if(word[5] in self.C2 and word[6] == self.tashkeel['a']):  # noqa
                            if(word[7] == self.constants['a2']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_1_8_word(word)

    def case_b_2_1(self, word):
        # انفطر
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] == self.constants['B4']):  # noqa
                        if(word[2] in self.C1 and word[2] != self.constants['B3']):
                            if(word[3] in self.C2):
                                if(word[4] in self.C3):
                                    return True

        def check2(word):
            if(len(word) == 9):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] == self.constants['B4'] and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] in self.C1 and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C2 and word[6] != self.constants['B3'] and word[7] == self.tashkeel['a']):  # noqa
                                if(word[8] in self.C3):
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_2_1_word(word)

    def case_b_2_2(self, word):
        # انبث
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] == self.constants['B4']):  # noqa
                        if(word[2] in self.C1):
                            if(word[3] in self.C2 and word[4] == self.tashkeel['d']):  # noqa
                                return True

        def check2(word):
            if(len(word) == 8):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] == self.constants['B4'] and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] in self.C1 and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C2 and word[7] == self.tashkeel['d']):  # noqa
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_2_2_word(word)

    def case_b_3_1(self, word):
        # تفقّد
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B3']):
                    if(word[1] in self.C1 or word[1] == self.constants['w']):  # noqa
                        if(word[2] in self.C2 and word[3] == self.tashkeel['d']):  # noqa
                            if(word[4] in self.C3):
                                return True

        def check2(word):
            if(len(word) == 8):
                word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
                if(word[0] == self.constants['B3'] and word[1] == self.tashkeel['a']):  # noqa
                    if((word[2] in self.C1 or word[2] == self.constants['w']) and word[3] == self.tashkeel['a']):  # noqa
                        if(word[4] in self.C2 and word[5] == self.tashkeel['d'] and word[6] == self.tashkeel['a']):  # noqa
                            if(word[7] in self.C3):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_3_1_word(word)

    def case_b_3_2(self, word):
        # أصّدّق
        def check1(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1 and word[2] == self.tashkeel['d']):  # noqa
                        if(word[3] in self.C2 and word[4] == self.tashkeel['d']):  # noqa
                            if(word[5] in self.C3):
                                return True

        def check2(word):
            if(len(word) == 9):
                word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['d'] and word[4] == self.tashkeel['a']):  # noqa
                        if(word[5] in self.C2 and word[6] == self.tashkeel['d'] and word[7] == self.tashkeel['a']):  # noqa
                            if(word[8] in self.C3):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_3_2_word(word)

    def case_b_3_3(self, word):
        # نلقّى توفّى
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B3']):
                    if(word[1] in self.C1 or word[1] == self.constants['w']):  # noqa
                        if(word[2] in self.C2 and word[3] == self.tashkeel['d']):  # noqa
                            if(word[4] == self.constants['a2']):
                                return True

        def check2(word):
            if(len(word) == 8):
                word = word.replace(self.tashkeel['a'] + self.tashkeel['d'], self.tashkeel['d'] + self.tashkeel['a'])  # noqa
                if(word[0] == self.constants['B3'] and word[1] == self.tashkeel['a']):  # noqa
                    if((word[2] in self.C1 or word[2] == self.constants['w']) and word[3] == self.tashkeel['a']):  # noqa
                        if(word[4] in self.C2 and word[5] == self.tashkeel['d'] and word[6] == self.tashkeel['a']):  # noqa
                            if(word[7] == self.constants['a2']):
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_3_3_word(word)

    def case_b_4_1(self, word):
        # تنافس
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B3']):
                    if(word[1] in self.C1):
                        if(word[2] == self.constants['aa']):
                            if(word[3] in self.C2 or word[3] == self.constants['w']):  # noqa
                                if(word[4] in self.C3):
                                    return True

        def check2(word):
            if(len(word) == 8):
                if(word[0] == self.constants['B3'] and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['a']):
                        if(word[4] == self.constants['aa']):
                            if((word[5] in self.C2 or word[5] == self.constants['w']) and word[6] == self.tashkeel['a']):  # noqa
                                if(word[7] in self.C3):
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_4_1_word(word)

    def case_b_4_2(self, word):
        # تعالى
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B3']):
                    if(word[1] in self.C1):
                        if(word[2] == self.constants['aa']):
                            if(word[3] in self.C2):  # noqa
                                if(word[4] == self.constants['a2']):
                                    return True

        def check2(word):
            if(len(word) == 8):
                if(word[0] == self.constants['B3'] and word[1] == self.tashkeel['a']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['a']):
                        if(word[4] == self.constants['aa']):
                            if(word[5] in self.C2 and word[6] == self.tashkeel['a']):  # noqa
                                if(word[7] == self.constants['a2']):
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_4_2_word(word)

    def case_b_5_1(self, word):
        # اسودّ
        w_root = self.get_root(self.clean2(word))
        if(w_root[-1] == w_root[-2]):
            return None
        def check1(word):
            if(len(word) == 5):
                if(word[0] == self.constants['B1']):
                    if(word[1] != self.constants['B4'] and word[1] in self.C1):
                        if(word[2] in self.C2 or word[2] == self.constants['w']):  # noqa
                            if(word[3] in self.C2 and word[4] == self.tashkeel['d']):  # noqa
                                return True

        def check2(word):
            if(len(word) == 8):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] != self.constants['B4'] and word[2] in self.C1 and word[3] == self.tashkeel['s']):  # noqa
                        if((word[4] in self.C2 or word[4] == self.constants['w']) and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C2 and word[7] == self.tashkeel['d']):  # noqa
                                return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_b_5_1_word(word)

    def case_c_1_1(self, word):
        # استغفر
        def check1(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B1']):
                    if(word[1] == self.constants['B2']):
                        if(word[2] == self.constants['B3']):  # noqa
                            if(word[3] in self.C1 or word[3] == self.constants['E1'] or word[3] == self.constants['y']):  # noqa
                                if(word[4] in self.C2):
                                    if(word[5] in self.C3 or word[5] == self.constants['E1']):  # noqa
                                        return True

        def check2(word):
            if(len(word) == 11):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] == self.constants['B2'] and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if((word[6] in self.C1 or word[6] == self.constants['E1'] or word[6] == self.constants['y']) and word[7] == self.tashkeel['s']):  # noqa
                                if(word[8] in self.C2 and word[9] == self.tashkeel['a']):  # noqa
                                    if(word[10] in self.C3 or word[10] == self.constants['E1']):  # noqa
                                        return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_c_1_1_word(word)

    def case_c_1_2(self, word):
        # استقرّ
        def check1(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B1']):
                    if(word[1] == self.constants['B2']):
                        if(word[2] == self.constants['B3']):  # noqa
                            if(word[3] in self.C1):  # noqa
                                if(word[4] in self.C2 and word[5] == self.tashkeel['d']):  # noqa
                                    return True

        def check2(word):
            if(len(word) == 10):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] == self.constants['B2'] and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C1 and word[7] == self.tashkeel['a']):  # noqa
                                if(word[8] in self.C2 and word[9] == self.tashkeel['d']):  # noqa
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_c_1_2_word(word)

    def case_c_1_3(self, word):
        # استقام
        def check1(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B1']):
                    if(word[1] == self.constants['B2']):
                        if(word[2] == self.constants['B3']):  # noqa
                            if(word[3] in self.C1):  # noqa
                                if(word[4] == self.constants['aa']):  # noqa
                                    if(word[5] in self.C2):
                                        return True

        def check2(word):
            if(len(word) == 10):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] == self.constants['B2'] and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] in self.C1 and word[7] == self.tashkeel['a']):  # noqa
                                if(word[8] == self.constants['aa']):  # noqa
                                    if(word[9] in self.C2):
                                        return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_c_1_3_word(word)

    def case_c_1_4(self, word):
        # استخفى
        def check1(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B1']):
                    if(word[1] == self.constants['B2']):
                        if(word[2] == self.constants['B3']):  # noqa
                            if(word[3] in self.C1 or word[3] == self.constants['w']):  # noqa
                                if(word[4] in self.C2):  # noqa
                                    if(word[5] == self.constants['a2']):
                                        return True

        def check2(word):
            if(len(word) == 11):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] == self.constants['B2'] and word[3] == self.tashkeel['s']):  # noqa
                        if(word[4] == self.constants['B3'] and word[5] == self.tashkeel['a']):  # noqa
                            if((word[6] in self.C1 or word[6] == self.constants['w']) and word[7] == self.tashkeel['s']):  # noqa
                                if(word[8] in self.C2 and word[9] == self.tashkeel['a']):  # noqa
                                    if(word[10] == self.constants['a2']):
                                        return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_c_1_4_word(word)

    def case_c_2_1(self, word):
        # ادهامّ
        def check1(word):
            if(len(word) == 6):
                if(word[0] == self.constants['B1']):
                    if(word[1] in self.C1):
                        if(word[2] in self.C2):  # noqa
                            if(word[3] == self.constants['aa']):  # noqa
                                if(word[4] in self.C3):  # noqa
                                    return True

        def check2(word):
            if(len(word) == 9):
                if(word[0] == self.constants['B1'] and word[1] == self.tashkeel['i']):  # noqa
                    if(word[2] in self.C1 and word[3] == self.tashkeel['s']):
                        if(word[4] in self.C2 and word[5] == self.tashkeel['a']):  # noqa
                            if(word[6] == self.constants['aa']):  # noqa
                                if(word[7] in self.C3 and word[8] == self.tashkeel['d']):  # noqa
                                    return True

        check2 = check2(word)
        check1 = check1(word)
        isTashkeel = [True for t in self.tashkeel.values() if t in word and t != self.tashkeel['d']]  # noqa
        if(check2 or (check1 and len(isTashkeel) == 0)):
            return self.generate_case_c_2_1_word(word)

    def generate_case_a_1_1_word(self, word):
        source_word = word
        word = self.clean(word)
        case = self.cases['case_a_1_1']
        tmp = []
        C1 = word[1]
        C2 = word[2]
        C3 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        # اذا كان الحرف الثاني ياء
        if(word[1] == self.constants['y']):
            case = self.cases['case_a_1_1y']
            tmp[2] = self.constants['w']

        if(word[1] == self.constants['w']):
            case = self.cases['case_a_1_1w']

        tmp.append(self.tashkeel['s'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_a_1_2_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['i'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_a_1_2']}  # noqa

    def generate_case_a_1_3_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['E3'])
        tmp.append(self.tashkeel['s'])
        tmp.append(C1)
        tmp.append(self.tashkeel['i'])
        tmp.append(C2)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_a_1_3']}  # noqa

    def generate_case_a_1_4_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['s'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(self.constants['E2'])
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_a_1_4']}  # noqa

    def generate_case_a_1_5_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C3 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['i'])
        tmp.append(self.constants['y'])
        tmp.append(C3)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_a_1_5']}  # noqa

    def generate_case_a_1_6_word(self, word):
        case = self.cases['case_a_1_6a']
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[1]
        C2 = word[2]
        # مخز بتنوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['s'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['ni'])
        # مخزي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['s'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المخزي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['s'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])
        if(C1 == self.constants['w']):
            case = self.cases['case_a_1_6f']
        if(C2 == self.constants['w']):
            case = self.cases['case_a_1_6e']
        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa  # noqa

    def generate_case_a_1_7_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[1]
        # مؤت بتنوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(self.constants['E3'])
        tmp1.append(self.tashkeel['s'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['ni'])
        # مؤتي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(self.constants['E3'])
        tmp2.append(self.tashkeel['s'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المؤتي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(self.constants['E3'])
        tmp3.append(self.tashkeel['s'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])

        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': self.cases['case_a_1_7']}  # noqa  # noqa

    def generate_case_a_2_1_word(self, word):
        # أذن
        case = self.cases['case_a_2_1']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[0]
        C2 = word[1]
        C3 = word[2]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        if(C1 == self.constants['E1']):
            case = self.cases['case_a_2_1a']
            tmp[2] = self.constants['E3']
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        if(C2 == self.constants['y']):
            case = self.cases['case_a_2_1jy']
        if(C2 == self.constants['w']):
            case = self.cases['case_a_2_1jw']
        if(C2 == C3):
            case = self.cases['case_a_2_1d']
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_a_2_2_word(self, word):
        # صلى
        case = self.cases['case_a_2_1']
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[0]
        C2 = word[1]
        C3 = word[2]
        # مصل بتنوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['a'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['d'])
        tmp1.append(self.tashkeel['ni'])
        # مصلي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['a'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['d'])
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المصلي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['a'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['d'])
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])

        if(C1 == self.constants['w']):
            case = self.cases['case_a_2_2wa']
        elif(C3 == self.constants['a2']):
            case = self.cases['case_a_2_2a']
        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa  # noqa

    def generate_case_a_3_1_word(self, word):
        # واقع
        case = self.cases['case_a_3_1']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[0]
        C2 = word[2]
        C3 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['a'])
        tmp.append(self.constants['aa'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        if(C1 == self.constants['w']):
            case = self.cases['case_a_3_1w']
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_a_3_2_word(self, word):
        # ضارّ
        case = self.cases['case_a_3_2']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[0]
        C2 = word[2]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['a'])
        tmp.append(self.constants['aa'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_a_3_3_word(self, word):
        # نادى
        case = self.cases['case_a_3_3']
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[0]
        C2 = word[2]
        # مناد بتنوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['a'])
        tmp1.append(self.constants['aa'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['ni'])
        # منادي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['a'])
        tmp2.append(self.constants['aa'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المنادي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['a'])
        tmp3.append(self.constants['aa'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])

        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa  # noqa

    def generate_case_b_1_1_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[3]
        C3 = word[4]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['s'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_1_1']}  # noqa

    def generate_case_b_1_2_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        C3 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['d'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_1_2']}  # noqa

    def generate_case_b_1_3_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['s'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_1_3']}  # noqa

    def generate_case_b_1_4_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C2 = word[3]
        C3 = word[4]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['E3'])
        tmp.append(self.tashkeel['s'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_1_4']}  # noqa

    def generate_case_b_1_5_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['d'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(self.constants['E2'])
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_1_5']}  # noqa

    def generate_case_b_1_6_word(self, word):
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[4]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['s'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(self.constants['aa'])
        tmp.append(C2)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_1_6']}  # noqa

    def generate_case_b_1_7_word(self, word):
        # اهتدى
        case = self.cases['case_b_1_7']
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[1]
        C2 = word[3]
        # مهتد بتنوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['s'])
        tmp1.append(self.constants['B3'])
        tmp1.append(self.tashkeel['a'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['ni'])
        # مهتدي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['s'])
        tmp2.append(self.constants['B3'])
        tmp2.append(self.tashkeel['a'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المهتدي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['s'])
        tmp3.append(self.constants['B3'])
        tmp3.append(self.tashkeel['a'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])
        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa  # noqa

    def generate_case_b_1_8_word(self, word):
        # اتقى
        case = self.cases['case_b_1_8']
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[1]
        C2 = word[2]
        # متق بتنوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['d'])
        tmp1.append(self.tashkeel['a'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['ni'])
        # متقي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['d'])
        tmp2.append(self.tashkeel['a'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المتقي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['d'])
        tmp3.append(self.tashkeel['a'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])

        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa  # noqa

    def generate_case_b_2_1_word(self, word):
        # انفطر
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[2]
        C2 = word[3]
        C3 = word[4]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['B4'])
        tmp.append(self.tashkeel['s'])
        tmp.append(C1)
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_2_1']}  # noqa

    def generate_case_b_2_2_word(self, word):
        # انبث
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[2]
        C2 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['B4'])
        tmp.append(self.tashkeel['s'])
        tmp.append(C1)
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])
        return {'word': source_word, 'results': [''.join(tmp)], 'case': self.cases['case_b_2_2']}  # noqa

    def generate_case_b_3_1_word(self, word):
        # تفقّد
        case = self.cases['case_b_3_1']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        C3 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C1)
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        if(C1 == self.constants['w']):
            case = self.cases['case_b_3_1w']
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_b_3_2_word(self, word):
        # اصّدّق
        case = self.cases['case_b_3_2']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        C3 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['d'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_b_3_3_word(self, word):
        # توفى تلقى
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[1]
        C2 = word[2]
        # متوف بتوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(self.constants['B3'])
        tmp1.append(self.tashkeel['a'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['a'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['d'])
        tmp1.append(self.tashkeel['ni'])
        # متوفي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(self.constants['B3'])
        tmp2.append(self.tashkeel['a'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['a'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['d'])
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المتوفي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(self.constants['B3'])
        tmp3.append(self.tashkeel['a'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['a'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['d'])
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])
        if(C1 == self.constants['w']):
            case = self.cases['case_b_3_3w']
        else:
            case = self.cases['case_b_3_3a']

        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa

    def generate_case_b_4_1_word(self, word):
        # تنافس
        case = self.cases['case_b_4_1']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[3]
        C3 = word[4]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C1)
        tmp.append(self.tashkeel['a'])
        tmp.append(self.constants['aa'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)
        if(C2 == self.constants['w']):
            case = self.cases['case_b_4_1w']
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_b_4_2_word(self, word):
        # تعالى
        case = self.cases['case_b_4_2']
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[1]
        C2 = word[3]
        # متعال بتنوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(self.constants['B3'])
        tmp1.append(self.tashkeel['a'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['a'])
        tmp1.append(self.constants['aa'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['ni'])
        # متعالي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(self.constants['B3'])
        tmp2.append(self.tashkeel['a'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['a'])
        tmp2.append(self.constants['aa'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المتعالي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(self.constants['B3'])
        tmp3.append(self.tashkeel['a'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['a'])
        tmp3.append(self.constants['aa'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])

        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa

    def generate_case_b_5_1_word(self, word):
        # اسود
        case = self.cases['case_b_5_1']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        C3 = word[3]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['s'])
        tmp.append(C2)
        tmp.append(self.tashkeel['a'])
        tmp.append(C3)
        tmp.append(self.tashkeel['d'])
        if(C2 == self.constants['w']):
            case = self.cases['case_b_5_1w']
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_c_1_1_word(self, word):
        # استغفر
        case = self.cases['case_c_1_1']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[3]
        C2 = word[4]
        C3 = word[5]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['B2'])
        tmp.append(self.tashkeel['s'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C1)
        tmp.append(self.tashkeel['s'])
        tmp.append(C2)
        tmp.append(self.tashkeel['i'])
        tmp.append(C3)

        if(C1 == self.constants['E1']):
            case = self.cases['case_c_1_1af']
        elif(C1 == self.constants['y']):
            case = self.cases['case_c_1_1y']
        if(C3 == self.constants['E1']):
            tmp[-1] = self.constants['E2']
            case = self.cases['case_c_1_1al']
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_c_1_2_word(self, word):
        # استقرّ
        case = self.cases['case_c_1_2']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[3]
        C2 = word[4]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['B2'])
        tmp.append(self.tashkeel['s'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C1)
        tmp.append(self.tashkeel['i'])
        tmp.append(C2)
        tmp.append(self.tashkeel['d'])

        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_c_1_3_word(self, word):
        # استقام
        case = self.cases['case_c_1_3']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[3]
        C2 = word[5]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(self.constants['B2'])
        tmp.append(self.tashkeel['s'])
        tmp.append(self.constants['B3'])
        tmp.append(self.tashkeel['a'])
        tmp.append(C1)
        tmp.append(self.tashkeel['i'])
        tmp.append(self.constants['y'])
        tmp.append(C2)
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def generate_case_c_1_4_word(self, word):
        # استخفى
        case = self.cases['case_c_1_4']
        source_word = word
        word = self.clean(word)
        tmp1 = []
        tmp2 = []
        tmp3 = []
        C1 = word[3]
        C2 = word[4]
        # مستخف بتوين الكسر
        tmp1.append(self.constants['m'])
        tmp1.append(self.tashkeel['u'])
        tmp1.append(self.constants['B2'])
        tmp1.append(self.tashkeel['s'])
        tmp1.append(self.constants['B3'])
        tmp1.append(self.tashkeel['a'])
        tmp1.append(C1)
        tmp1.append(self.tashkeel['s'])
        tmp1.append(C2)
        tmp1.append(self.tashkeel['ni'])
        # مستخفي
        tmp2.append(self.constants['m'])
        tmp2.append(self.tashkeel['u'])
        tmp2.append(self.constants['B2'])
        tmp2.append(self.tashkeel['s'])
        tmp2.append(self.constants['B3'])
        tmp2.append(self.tashkeel['a'])
        tmp2.append(C1)
        tmp2.append(self.tashkeel['s'])
        tmp2.append(C2)
        tmp2.append(self.tashkeel['i'])
        tmp2.append(self.constants['y'])
        # المستخفي
        tmp3.append(self.constants['AL'])
        tmp3.append(self.constants['m'])
        tmp3.append(self.tashkeel['u'])
        tmp3.append(self.constants['B2'])
        tmp3.append(self.tashkeel['s'])
        tmp3.append(self.constants['B3'])
        tmp3.append(self.tashkeel['a'])
        tmp3.append(C1)
        tmp3.append(self.tashkeel['s'])
        tmp3.append(C2)
        tmp3.append(self.tashkeel['i'])
        tmp3.append(self.constants['y'])
        if(C1 == self.constants['w']):
            case = self.cases['case_c_1_4f']
        return {'word': source_word, 'results': [''.join(tmp1), ''.join(tmp2), ''.join(tmp3)], 'case': case}  # noqa

    def generate_case_c_2_1_word(self, word):
        # ادهام
        case = self.cases['case_c_2_1']
        source_word = word
        word = self.clean(word)
        tmp = []
        C1 = word[1]
        C2 = word[2]
        C3 = word[4]
        tmp.append(self.constants['m'])
        tmp.append(self.tashkeel['u'])
        tmp.append(C1)
        tmp.append(self.tashkeel['s'])
        tmp.append(C2)
        tmp.append(self.tashkeel['a'])
        tmp.append(self.constants['aa'])
        tmp.append(C3)
        tmp.append(self.tashkeel['d'])
        return {'word': source_word, 'results': [''.join(tmp)], 'case': case}  # noqa

    def test(self, word):
        word = word.strip()
        solve = [r for r in
                 [
                  # Main A Case 1
                  self.case_a_1_1_v2(word),
                  self.case_a_1_2(word),
                  self.case_a_1_3(word),
                  self.case_a_1_4(word),
                  self.case_a_1_5(word),
                  self.case_a_1_6(word),
                  self.case_a_1_7(word),
                  # Main A Case 2
                  self.case_a_2_1(word),
                  self.case_a_2_2(word),
                  # Main A Case3
                  self.case_a_3_1(word),
                  self.case_a_3_2(word),
                  self.case_a_3_3(word),
                  # Main B case1
                  self.case_b_1_1(word),
                  self.case_b_1_2(word),
                  self.case_b_1_3(word),
                  self.case_b_1_4(word),
                  self.case_b_1_5(word),
                  self.case_b_1_6(word),
                  self.case_b_1_7(word),
                  self.case_b_1_8(word),
                  # Main B case2
                  self.case_b_2_1(word),
                  self.case_b_2_2(word),
                  # Main B case3
                  self.case_b_3_1(word),
                  self.case_b_3_2(word),
                  self.case_b_3_3(word),
                  # Main B case4
                  self.case_b_4_1(word),
                  self.case_b_4_2(word),
                  # Main B case5
                  self.case_b_5_1(word),
                  # Main C case1
                  self.case_c_1_1(word),
                  self.case_c_1_2(word),
                  self.case_c_1_3(word),
                  self.case_c_1_4(word),
                  # Main C case2
                  self.case_c_2_1(word),
                  ] if r is not None]
        if(len(solve) > 0):
            return solve
