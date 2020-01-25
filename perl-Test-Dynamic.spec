#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Dynamic
Summary:	Test::Dynamic - Automatic test counting for Test::More
#Summary(pl.UTF-8):	
Name:		perl-Test-Dynamic
Version:	1.3.3
Release:	1
License:	bsd
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1f92a8c14584d45b12d31e5ed942d4c
URL:		http://search.cpan.org/dist/Test-Dynamic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module helps to count your tests for you in an automatic way.  When
you add or remove tests, Test::Dynamic will attempt to keep track of
the total correct number for you.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
