# http://github.com/spf13/viper
%global goipath         github.com/spf13/viper
%global gcommit         25b30aa063fc18e48662b86996252eabdcf2f0c7
Version:        1.0.0

%gometa

Name:           %{goname}
Release:        3%{?dist}
Summary:        Go configuration with fangs
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/fsnotify/fsnotify)
BuildRequires: golang(github.com/hashicorp/hcl)
BuildRequires: golang(github.com/magiconair/properties)
BuildRequires: golang(github.com/mitchellh/mapstructure)
BuildRequires: golang(github.com/pelletier/go-toml)
BuildRequires: golang(github.com/spf13/afero)
BuildRequires: golang(github.com/spf13/cast)
BuildRequires: golang(github.com/spf13/jwalterweatherman)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(gopkg.in/yaml.v2)
# tests
BuildRequires: golang(github.com/stretchr/testify/assert)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup

%install
rm -rf remote
# source codes for building projects
%goinstall

%check
#constant 765432101234567 overflows int
%ifarch %{ix86} || %{arm}
%gochecks -d .
%else
%gochecks
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-2.git25b30aa
- Update to spec 3.0

* Wed Feb 21 2018 Kaushal <kshlmster@gmail.com> - 1.0.0-1
- Update to upstream v1.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitc1de958
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitc1de958
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitc1de958
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gitc1de958
- Bump to upstream c1de95864d73a5465492829d7cb2dd422b19ac96
  related: #1414254

* Mon Mar 06 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.git1699063
- Use the default weather import path prefix
  related: #1414254

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git1699063
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git1699063
- Bump to upstream 16990631d4aa7e38f73dbbbf37fa13e67c648531
  resolves: #1414254

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitbe5ff3e
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitbe5ff3e
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitbe5ff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitbe5ff3e
- First package for Fedora
  resolves: #1270064
