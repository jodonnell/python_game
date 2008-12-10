/System/Library/Frameworks/Python.framework/Versions/2.5/Resources/Python.app/Contents/MacOS/Python setup.py install --root=$RPM_BUILD_ROOT

cat >INSTALLED_FILES <<EOF
%doc Demo
EOF
find $RPM_BUILD_ROOT -type f | sed -e "s|$RPM_BUILD_ROOT||g" >>INSTALLED_FILES

